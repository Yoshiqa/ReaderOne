from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.product_page import ProductPage


def test_buy_book(set_up):
    print('Start test_buy_book')

    driver = set_up

    mp = MainPage(driver)
    mp.go_to_the_catalog()

    cp = CatalogPage(driver)
    cp.go_to_category_paperwhite_book()
    cp.go_to_category_paperwhite_book_2024()
    cp.go_to_product_1_in_category_paperwhite_book_2024()

    pp = ProductPage(driver)
    product_name, product_price = pp.buy_product()

    cart = CartPage(driver)
    product_name_cart, product_price_cart = cart.checkout_product()

    assert product_name == product_name_cart, 'The product name in Cart is different'
    assert product_price == product_price_cart, 'The product price in Cart is different'

    op = OrderPage(driver)
    product_name_order, product_price_order = op.place_an_order()

    assert product_name == product_name_order, 'The product name in Order is different'
    assert product_price == product_price_order, 'The product price in Order is different'
