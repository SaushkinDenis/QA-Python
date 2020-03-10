import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="safari", help="Web Browser")
    parser.addoption("--wait", action="store", default="60", help="Set wait")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "safari":
        wd = webdriver.Safari()
    elif browser == "chrome":
        op = webdriver.ChromeOptions()
        wd = webdriver.Chrome(executable_path='/Users/sauskindenis/Desktop/webdrivers/chromedriver', options=op)
    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        wd = webdriver.Firefox(options=op)
    else:
        wd = webdriver.Safari()

    wd.maximize_window()

    yield wd
    wd.quit()


@pytest.fixture
def waits(request):
    wait = request.config.getoption("--wait")
    return int(wait)
