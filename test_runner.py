import pytest
import os

from plugins.exception_plugin import ExceptionPlugin


def run_test(command_name, email, amount=1):
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.chdir(test_dir)

    pytest_args = ['-v', f'test_{command_name}.py', '--email', email, '--amount', amount]
    plugin = ExceptionPlugin()
    result = pytest.main(pytest_args, plugins=[plugin])

    return result, plugin.failures
