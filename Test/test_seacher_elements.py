import time

from selenium.webdriver.common.by import By


def test_find_elements_title(browser):
    url = "https://demo.opencart.com/"
    title_original = "Your Store"

    driver = browser
    driver.get(url)
    time.sleep(5)
    title = find_locator(driver, "#logo > h1 > a").text
    search_field = find_locator(driver, "#content > h3")
    contact_phone = find_locator(driver, "#top-links > ul > li:nth-child(1) > a > i")
    shopping_basket_buttom = find_locator(driver, "#cart > button")
    mp3_players_menu_buttom = find_locator(driver, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(8) > a")
    mp3_players_menu_buttom.click()
    mp3_players_list = driver.find_elements_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li.dropdown.open > div > div")

# def test_find_elements_thing():
#
# def test_find_elements_catalog():
#
# def test_find_elements_login_admin():
#
# def test_find_elements_result_of_found():
#   search = find_locator(driver, "#content > h3")
#   search.send_keys("test")
#   find_locator(driver, "#content > p:nth-child(7)").text == "There is no product that matches the search criteria."


def find_locator(driver, locator):
    return driver.find_element_by_css_selector(locator)
