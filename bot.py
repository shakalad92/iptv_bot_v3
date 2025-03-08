import asyncio
import logging
import os
import pytest
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.filters.command import CommandObject
from aiogram.types import Message
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

def generate_pytest_args(command_name: str, args: list) -> list:
    command_config = {
        "create": ["--phone_number", "--amount"],
        "recharge": ["--email", "--amount"],
        "activate": ["--email"],
        "cplayer": ["--email", "--playlist_link"],
        "alink": ["--email", "--playlist_link"],
        "ctest": ["--phone_number"]
    }

    # pytest_args = ['--headed', '-v', f'test_{command_name}.py']
    pytest_args = ['--headed', '-v', '--browser-args="--no-sandbox,--disable-dev-shm-usage"', f'test_{command_name}.py']
    arg_keys = command_config.get(command_name)

    if not arg_keys:
        raise ValueError(f"Unknown command: {command_name}")

    if len(args) != len(arg_keys):
        raise ValueError(f"Command /{command_name} requires {len(arg_keys)} arguments: {command_config[command_name]}")

    for key, value in zip(arg_keys, args):
        pytest_args.extend([key, value])

    return pytest_args

def run_test(command_name, *args):
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.chdir(test_dir)

    try:
        pytest_args = generate_pytest_args(command_name, args)
        print(f"Running Pytest with arguments: {pytest_args}")
        result = pytest.main(pytest_args)
        return result
    except Exception as e:
        print(f"Error running test: {e}")
        return 1

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("IPService bot is now active!")

@dp.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    help_text = (
        "Welcome to the IPService bot! Here are the available commands:\n\n"
        "📌 **To create a user with payment**:\n"
        "   `/create <phone_number> <amount>`\n"
        "   Example: `/create 555386726 1`\n\n"
        "📌 **To recharge a user's balance**:\n"
        "   `/recharge <email> <amount>`\n"
        "   Example: `/recharge email@gmail.com 1`\n\n"
        "📌 **To check admin balance**:\n"
        "   `/balance`\n\n"
        "📌 **To create a test user without payment**:\n"
        "   `/ctest <phone_number>`\n"
        "   Example: `/create 555386726`\n\n"
        "📌 **To attach a link to a player**:\n"
        "   `/alink <email> <link>`\n"
        "   Example: `/alink email@gmail.com https://example.com`\n\n"
        "📌 **To create a user in the player and attach a link**:\n"
        "   `/cplayer <email> <playlist_link>`\n"
        "   Example: `/cplayer email@gmail.com playlist_link`\n\n"
    )
    await message.reply(help_text, parse_mode="Markdown")


@dp.message(Command(commands=['create', 'recharge', 'activate', 'cplayer', 'ctest', 'alink']))
async def handle_command(message: Message, command: CommandObject):
    command_name = command.command
    args = command.args

    if not args:
        await message.reply(f"Please enter the required arguments after the /{command_name} command.")
        return

    args_list = args.split()

    try:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, run_test, command_name, *args_list)

        if result == 0:
            await message.reply(f"✅ Test `{command_name}` successfully passed!")
        else:
            await message.reply(f"❌ Test `{command_name}` failed with errors. Check logs for details.")
    except ValueError as e:
        await message.reply(f"⚠️ Error: {str(e)}")
    except Exception as e:
        await message.reply(f"❌ An unexpected error occurred: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")