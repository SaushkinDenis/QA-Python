import argparse
import logging

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file", default=None)
args = parser.parse_args()
logging.basicConfig(filename=args.file, level=logging.INFO)


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
        driver.save_screenshot(f'Test/Logs/exception ' + exception + '.png')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Web Browser")
    parser.addoption("--wait", action="store", default="60", help="Set wait")


@pytest.fixture
def browser(request):
    logger = logging.getLogger('Driver')
    browser = request.config.getoption("--browser")
    if browser == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()
    elif browser == "chrome":
        # options.add_argument("--kiosk")
        # options.add_argument("--start-maximized")
        desired = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        desired['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        driver = EventFiringWebDriver(webdriver.Chrome(executable_path='Common/webdrivers/chromedriver', desired_capabilities=desired, options=options), Listener())
    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        driver = webdriver.Firefox(options=op)
    else:
        driver = webdriver.Safari()
        driver.maximize_window()

    logger.info('\n Running ' + __name__)
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
def waits(request):
    wait = request.config.getoption("--wait")
    return int(wait)


