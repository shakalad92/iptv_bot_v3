import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.filters.command import CommandObject
from aiogram.types import Message

from config import TELEGRAM_TOKEN
from test_runner import run_test

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("IPSERVICE bot is now active")


@dp.message(Command(commands=['create', 'recharge', 'activate']))
async def handle_message(message: Message, command: CommandObject):
    command_name = command.command
    args = command.args

    if not args:
        await message.reply(f"Please enter the email after the /{command_name} command. For example /{command_name} mishka_ylea@gmail.com")
        return

    if len(args) > 1:
        email, amount = args.split()

        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, run_test, command_name, email, amount)

        if result == 0:
            await message.reply(f"Тест {command_name} успешно пройден для {email}")
        else:
            await message.reply(f"Тест {command_name} не пройден для {email}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
