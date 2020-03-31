import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="safari", help="Web Browser")
    parser.addoption("--wait", action="store", default="60", help="Set wait")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "safari":
        driver = webdriver.Safari()
    elif browser == "chrome":
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='/Users/sauskindenis/Desktop/webdrivers/chromedriver', options=op)
    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        driver = webdriver.Firefox(options=op)
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    url = {'css': 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'}
    driver.get(url['css'])

    yield driver
    driver.quit()


@pytest.fixture
def waits(request):
    wait = request.config.getoption("--wait")
    return int(wait)
