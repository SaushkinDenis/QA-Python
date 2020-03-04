from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_find_elements_title(browser):
    url = "https://demo.opencart.com/"
    logo_correct = "Your Store"
    search = "Search"
    phone_attr = "fa fa-phone"
    locator_title = "#logo > h1 > a"
    locator_search = "#search > input"
    locator_contact_phone = "#top-links > ul > li:nth-child(1) > a > i"
    locator_shopping_busket = "#cart > button"
    locator_mp3_player_menu = "li:nth-child(8) > a"

    driver = browser
    driver.get(url)

    title = find_locator(driver, locator_title)
    search_field = find_locator(driver, locator_search)
    contact_phone = find_locator(driver, locator_contact_phone)
    shopping_basket_button = find_locator(driver, locator_shopping_busket)
    mp3_players_menu_button = find_locator(driver, locator_mp3_player_menu)

    assert title.text == logo_correct
    assert search_field.get_attribute("placeholder") == search
    assert contact_phone.get_attribute("class") == phone_attr
    assert shopping_basket_button.is_displayed()
    assert mp3_players_menu_button.tag_name == "a"


def test_find_elements_thing(browser):
    url = "https://demo.opencart.com/index.php?route=product/product&product_id=40"
    like = "fa fa-heart"
    phone = "Apple"
    price_current = "$123.20"
    resource = "https://demo.opencart.com/image/cache/catalog/demo/iphone_1-228x228.jpg"
    value_qty = "1"

    locator_like_button = "#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1) > i"
    locator_brand = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(1) > a"
    locator_price = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2"
    locator_image = "#content > div:nth-child(1) > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img"
    locator_qty_text = "#input-quantity"

    driver = browser
    driver.get(url)

    like_button = find_locator(driver, locator_like_button)
    brand = find_locator(driver, locator_brand)
    price = find_locator(driver, locator_price)
    image = find_locator(driver, locator_image)
    qty = find_locator(driver, locator_qty_text)

    assert like_button.get_attribute("class") == like
    assert brand.text == phone
    assert price.text == price_current
    assert image.get_attribute("src") == resource
    assert qty.get_attribute("value") == value_qty


def test_find_elements_catalog(browser):
    url = "https://demo.opencart.com/index.php?route=product/category&path=18"

    resource = "https://demo.opencart.com/image/cache/catalog/demo/hp_2-80x80.jpg"
    default = "Default"
    button = "button"

    locator_list_group = "#column-left > div.list-group"
    locator_image = "#content > div:nth-child(2) > div.col-sm-2 > img"
    locator_view_list = "#list-view"
    locator_sort = "#input-sort"
    locator_buy_thing = "#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)"

    driver = browser
    driver.get(url)

    list_group = find_locator(driver, locator_list_group)
    image = find_locator(driver, locator_image)
    view_list = find_locator(driver, locator_view_list)
    sort = find_locator(driver, locator_sort)
    buy_thing = find_locator(driver, locator_buy_thing)

    assert list_group.is_displayed()
    assert image.get_attribute("src") == resource
    assert view_list.is_enabled()
    assert sort.find_element_by_css_selector("option:nth-child(1)").text == default
    assert buy_thing.get_attribute("type") == button


def test_find_elements_login_admin(browser):
    url = "https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=xphNMI2SAuc5GTHg2jFidh00bO2XAhCq"

    catalog = "Catalog"
    attrib = "pull-right"

    locator_auth = "#content > div > div > div > div > div.panel-body > form > div.text-right > button"
    locator_catalog_button = "#menu-catalog > a"
    locator_progress = "#stats > ul > li:nth-child(1) > div.progress > div"
    locator_settings_button = "#button-setting"
    locator_total_order_text = "#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-body > h2"
    locator_zoom_button = "#vmap > div.jqvmap-zoomin"

    driver = browser
    driver.get(url)
    find_locator(driver, locator_auth).click()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable ((By.CSS_SELECTOR, locator_zoom_button)))

    catalog_button = find_locator(driver, locator_catalog_button)
    progress = find_locator(driver, locator_progress)
    settings_button = find_locator(driver, locator_settings_button)
    total_order_text = find_locator(driver, locator_total_order_text)
    zoom_button = find_locator(driver, locator_zoom_button)

    assert catalog_button.text == catalog
    assert progress.get_attribute("aria-valuenow") == "0"
    assert settings_button.is_enabled()
    assert total_order_text.get_attribute("class") == attrib
    assert zoom_button.is_enabled()


def test_find_elements_result_of_found(browser):
    url = "https://demo.opencart.com/index.php?route=product/search&search=apple"
    apple = "apple"
    length_list_category = 39
    resource = "https://demo.opencart.com/index.php?route=product/product&product_id=42&search=apple"

    locator_found_text = "#input-search"
    locator_category_list = "#content > div:nth-child(3) > div:nth-child(2) > select"
    locator_flag_desc = "#description"
    locator_research_button = "#button-search"
    locator_first_result = "#content > div:nth-child(8) > div"

    driver = browser
    driver.get(url)

    found_text = find_locator(driver, locator_found_text)
    category_list = find_locator(driver, locator_category_list)
    flag_desc = find_locator(driver, locator_flag_desc)
    research_button = find_locator(driver, locator_research_button)
    first_result = find_locator(driver, locator_first_result)
    flag_desc.click()

    assert found_text.get_attribute("value") == apple
    assert len(category_list.find_elements_by_css_selector("option")) == length_list_category
    assert flag_desc.is_selected()
    assert research_button.is_enabled()
    assert first_result.find_element_by_css_selector("div > div.image > a").get_attribute("href") == resource


def find_locator(driver, locator):
    return driver.find_element_by_css_selector(locator)
