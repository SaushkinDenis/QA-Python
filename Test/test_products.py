from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_edit_elements_of_products(browser, waits):
    url = 'https://demo.opencart.com/admin/index.php?route=catalog/' \
          'product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'
    locator_auth = "div.panel-body > form > div.text-right > button"

    driver = browser
    wait = WebDriverWait(driver, waits)

    driver.get(url)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_auth)))
    element.submit()

    locator_products = "#form-product > div > table > tbody"
    locator_edit_product = "tr:nth-child(1) > td:nth-child(8) > a > i"
    locator_flag_product = "tr:nth-child(1) > td:nth-child(1) > input[type='checkbox']"
