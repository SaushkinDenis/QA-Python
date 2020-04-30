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
    parser.addoption("--executor", action="store", default="192.168.99.101")
    parser.addoption("--selenoid", default=True)


@pytest.fixture
def browser(request):
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
            webdriver.Chrome(executable_path='Common/files/chromedriver', desired_capabilities=desired,
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
def remote(request):
    logger = logging.getLogger('Driver')
    logger.info('\n Running driver')

    # driver = get_remote_cloud()
    # driver = get_remote(request)

    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    capabilities = {
        "browserName": "chrome",
        "version": "81.0",
        "enableVNC": True,
        "enableVideo": False
    }
    # selenoid = request.config.getoption("--selenoid")
    driver = webdriver.Remote(
        command_executor="http://192.168.99.101:4444/wd/hub",
        desired_capabilities=capabilities)


    driver.maximize_window()
    URL = 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    driver.get(URL)

    request.addfinalizer(driver.quit)
    logger.info('Stopped driver')
    return driver


def get_remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    # selenoid = request.config.getoption("--selenoid")
    driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                              desired_capabilities={"browserName": {browser}})

    return driver


def get_remote_cloud():
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '81.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768',
        'name': 'QA-Testing-[Python] Test'
    }
    driver = webdriver.Remote(
        command_executor='http://kerryyos1:########.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)

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
