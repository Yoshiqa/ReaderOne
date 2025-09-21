from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CatalogPage(Base):
    # Locators
    category_paperwhite_book = '(//a[@href="/product/amazon/paperwhite/" and text()="Paperwhite"])[2]'
    category_paperwhite_book_2024 = '(//a[@href="/product/amazon/paperwhite/paperwhite12_2024/" and text()="2024"])[2]'
    product_1_in_category_paperwhite_book_2024 = '//li[@id="bx_3783077460_58280"]'

    # Getters
    def get_category_paperwhite_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_paperwhite_book)))

    def get_category_paperwhite_book_2024(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_paperwhite_book_2024)))

    def get_product_1_in_category_paperwhite_book_2024(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1_in_category_paperwhite_book_2024)))

    # Actions
    def click_category_paperwhite_book(self):
        self.get_category_paperwhite_book().click()
        print('click_category_paperwhite_book')

    def click_category_paperwhite_book_2024(self):
        self.get_category_paperwhite_book_2024().click()
        print('click_category_paperwhite_book_2024')

    def select_product_1_in_category_paperwhite_book_2024(self):
        self.get_product_1_in_category_paperwhite_book_2024().click()
        print('select_product_1_in_category_paperwhite_book_2024')

    # Methods
    def go_to_category_paperwhite_book(self):
        self.click_category_paperwhite_book()
        print('go_to_category_paperwhite_book')

    def go_to_category_paperwhite_book_2024(self):
        self.click_category_paperwhite_book_2024()
        print('go_to_category_paperwhite_book_2024')

    def go_to_product_1_in_category_paperwhite_book_2024(self):
        self.select_product_1_in_category_paperwhite_book_2024()
        print('go_to_product_1_in_category_paperwhite_book_2024')