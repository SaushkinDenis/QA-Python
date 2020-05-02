import argparse
import logging
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Web Browser",
                     choices=["chrome", "firefox", "safari"])
    parser.addoption("--wait", action="store", default="10", help="Set wait")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--selenoid", default=False)


@pytest.fixture
def browser_with_listner(request):
    logger = logging.getLogger('Driver')
    browser = request.config.getoption("--browser")
    if browser == "safari":
        driver = webdriver.Safari()

    elif browser == "chrome":
        desired = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        desired['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        driver = EventFiringWebDriver(
            webdriver.Chrome(executable_path='../Common/files/chromedriver', desired_capabilities=desired,
                             options=options), Listener())

    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        driver = webdriver.Firefox(options=op)

    else:
        driver = webdriver.Safari()

    driver.maximize_window()
    logger.info('\n Running driver')
    URL = 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    driver.get(URL)

    yield driver

    logger.info("\nConsole Logs")
    console_logs = driver.get_log("browser")
    for log in console_logs:
        logger.warning(log)

    driver.quit()
    logger.info('Stopped driver')


@pytest.fixture
def remote_browser(request):
    logger = logging.getLogger('Driver')
    logger.info('\n Running driver')

    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption("--selenoid")

    capabilities = {
        "browserName": browser,
        "enableVNC": True,
        "enableVideo": False
    }

    if selenoid:
        executor = "192.168.99.101"
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(executable_path='../Common/files/chromedriver')

    driver.maximize_window()
    URL = 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    driver.get(URL)

    request.addfinalizer(driver.quit)
    logger.info('Stopped driver')
    return driver


@pytest.fixture
def waits(request):
    wait = request.config.getoption("--wait")
    return int(wait)


# parser = argparse.ArgumentParser()
# parser.add_argument('-f', "--file", default=None)
# args = parser.parse_args()
# logging.basicConfig(filename=args.file, level=logging.INFO)
logging.basicConfig(filename=None, level=logging.INFO)


class Listener(AbstractEventListener):
    logger = logging.getLogger("BasicCommands")

    def after_navigate_to(self, url, browser):
        self.logger.info(f"Opened URL: {url} \n")

    def before_find(self, by, value, driver):
        self.logger.info(f"Find element: '{value}' with '{by}'")

    def after_click(self, element, driver):
        self.logger.info(f"Clicked element. \n ")

    def after_quit(self, driver):
        self.logger.info(f"Finished test")

    def on_exception(self, exception, driver):
        self.logger.error(f'Exception: {exception}')
        driver.save_screenshot(f'{exception}.png')
