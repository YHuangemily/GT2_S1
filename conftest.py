import pytest
import logging

log = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--ip", action="store",
                    help='IP address of the device')
    parser.addoption("--port", action="store",
                    help='port of the device')
    parser.addoption("--index", action="store",
                    help='Run test on specific sensor')

def pytest_generate_tests(metafunc):
    metafunc.parametrize("ip", [metafunc.config.getoption('ip')])
    metafunc.parametrize("port", [metafunc.config.getoption('port')])
    metafunc.parametrize("index", [metafunc.config.getoption('index')])
