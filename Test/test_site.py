from selenium.webdriver.common.by import By


def test_current_cite(browser):
    url = "https://demo.opencart.com/"
    current_title = "Your Store"
    print("\n Base URL: " + url)

    driver = browser
    driver.get(url)
    title = driver.title
    check_url = driver.current_url
    assert title == current_title and check_url == url


def find_css(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator)
