import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class _Findler:
    def __init__(self, locator):
        self._locator = locator

    def __call__(self, driver):
        element = None
        while not element:
            try:
                element = driver.find_element_by_css_selector(self._locator)
            except NoSuchElementException:
                time.sleep(0.2)
        return element


def test_wait_last_element(browser, waits):
    url = 'https://demo.opencart.com/admin/index.php?route=catalog/' \
          'product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    locator_auth = "div.panel-body > form > div.text-right > button"
    locator_edit_product = "tr:nth-child(19) > td:nth-child(8) > a > i"
    locator_currect_click = "#input-name1"

    driver = browser
    wait = WebDriverWait(driver, waits)

    driver.get(url)
    element = wait.until(_Findler(locator_auth))
    element.submit()

    wait.until(_Findler(locator_edit_product)).click()
    assert wait.until(_Findler(locator_currect_click)).get_attribute("value") == "Sony VAIO"


def test_wait_input_text(browser, waits):
    url = 'https://demo.opencart.com/admin/index.php?route=catalog/' \
          'product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    locator_auth = "div.panel-body > form > div.text-right > button"
    locator_text_product_name = "#input-name"
    locator_check_find = "#filter-product > div > div.panel-body > div:nth-child(1) > ul > li"
    locator_check_choose = "div.panel-body > div:nth-child(1) > ul > li > a"

    driver = browser
    wait = WebDriverWait(driver, waits)

    driver.get(url)
    element = wait.until(_Findler(locator_auth))
    element.submit()

    field_product_name = wait.until(_Findler(locator_text_product_name))
    field_product_name.send_keys("Sony")
    wait.until(_Findler(locator_check_find)).click()

    assert wait.until(_Findler(locator_check_choose)).text == "Sony VAIO"


def test_wait_select_status(browser, waits):
    url = 'https://demo.opencart.com/admin/index.php?route=catalog/' \
          'product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    locator_auth = "div.panel-body > form > div.text-right > button"
    locator_status = "#input-status"
    locator_click_value_status = "#input-status > option:nth-child(2)"

    driver = browser
    wait = WebDriverWait(driver, waits)

    driver.get(url)
    element = wait.until(_Findler(locator_auth))
    element.submit()

    wait.until(_Findler(locator_status)).click()
    wait.until(_Findler(locator_click_value_status)).click()

    assert wait.until(_Findler(locator_click_value_status)).is_selected()
