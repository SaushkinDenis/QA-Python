def test_find_elements_title(browser):
    url = "https://demo.opencart.com/"
    locator_title = "#logo > h1 > a"
    locator_search = "#content > h3"
    locator_contact_phone = "#top-links > ul > li:nth-child(1) > a > i"
    locator_shopping_busket = "#cart > button"
    locator_mp3_player_menu = "li:nth-child(8) > a"
    locator_mp3_player_list = "li.dropdown.open > div > div"

    driver = browser
    driver.get(url)

    title = find_locator(driver, locator_title).text
    search_field = find_locator(driver, locator_search)
    contact_phone = find_locator(driver, locator_contact_phone)
    shopping_basket_button = find_locator(driver, locator_shopping_busket)

    mp3_players_menu_button = find_locator(driver, locator_mp3_player_menu)
    mp3_players_menu_button.click()
    mp3_players_list = driver.find_elements_by_css_selector(locator_mp3_player_list)
    mp3_test = mp3_players_list[0]


def test_find_elements_thing(browser):
    url = "https://demo.opencart.com/index.php?route=product/product&product_id=40"
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


def test_find_elements_catalog(browser):
    url = "https://demo.opencart.com/index.php?route=product/category&path=18"
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


def test_find_elements_login_admin(browser):
    url = "https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=xphNMI2SAuc5GTHg2jFidh00bO2XAhCq"
    locator_catalog_button = "#menu-catalog > a"
    locator_progress = "#stats > ul > li:nth-child(1) > div.progress > div"
    locator_setting_button = "#button-setting"
    locator_total_order_text = "#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-body > h2"
    locator_zoom_button = "#vmap > div.jqvmap-zoomin"

    driver = browser
    driver.get(url)

    catalog_button = find_locator(driver, locator_catalog_button)
    progress = find_locator(driver, locator_progress)
    setting_button = find_locator(driver, locator_setting_button)
    total_order_text = find_locator(driver, locator_total_order_text)
    zoom_button = find_locator(driver, locator_zoom_button)


def test_find_elements_result_of_found(browser):
    url = "https://demo.opencart.com/index.php?route=product/search&search=apple"
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


def find_locator(driver, locator):
    return driver.find_element_by_css_selector(locator)
