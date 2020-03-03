import pyte
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="safari", help="Web Browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "safari":
        wd = webdriver.Safari()
    elif browser == "chrome":
        op = webdriver.ChromeOptions()
        # op.add_argument("headless")
        wd = webdriver.Chrome(executable_path="/Users/sauskindenis/Desktop/webdrivers/chromedriver.exec", options=op)
    elif browser == "ie":
        op = webdriver.IeOptions()
        op.add_argument("headless")
        wd = webdriver.Ie(options=op)
    elif browser == "firefox":
        op = webdriver.FirefoxOptions()
        op.add_argument("headless")
        wd = webdriver.Firefox(options=op)
    else:
        wd = webdriver.Safari()

    wd.maximize_window()
    yield wd
    wd.quit()
