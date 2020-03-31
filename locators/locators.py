class locators:

    class AdminPage:
        selector_auth = {'css': "div.panel-body > form > div.text-right > button"}
        selector_menu_catalog = {'css': "#menu-catalog > a"}
        selector_menu_products = {'css': "#collapse1 > li:nth-child(2) > a"}

    class ListProductsPage:
        url = {'css': 'https://demo.opencart.com/admin/index.php?route=catalog/product&user_token=vfru3mBkQg3TPmtnnD9wSBYYA8wCVXST'}

        selector_product = {'css': "#form-product > div > table > tbody > tr:nth-child(1)"}
        selector_edit_product_first = {'css': selector_product['css'] + " > td:nth-child(8) > a > i"}
        selector_flag_first_product = {'css': selector_product['css'] + " > td:nth-child(1) > input[type='checkbox']"}
        selector_button = {'css': "#content > div.page-header > div > div"}
        selector_add_product = {'css': selector_button['css'] + " > a"}
        selector_del_product = {'css': selector_button['css'] + " > button.btn.btn-danger"}
        selector_list_product = {'css': "#form-product > div > table > tbody > tr"}

    class ProductPage:
        selector_name_product = {'css': "#input-name1"}
        selector_product = {'css': "#language1 > div:nth-child(2) > div > div > div.note-toolbar.panel-heading > div.note-btn-group.btn-group.note-style > div"}
        selector_text_product_style = {'css': selector_product['css'] + " > button"}
        selector_text_product_style_blockquote = {'css': selector_product['css'] + " > div > li:nth-child(4) > a"}
        selector_product_save = {'css': "#content > div.page-header > div > div > button"}
