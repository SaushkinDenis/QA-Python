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
        driver = webdriver.Chrome(executable_path='/chromedriver', options=op)
    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        driver = webdriver.Firefox(options=op)
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    URL = 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    driver.get(URL)

    yield driver
    driver.quit()


@pytest.fixture
def waits(request):
    wait = request.config.getoption("--wait")
    return int(wait)
