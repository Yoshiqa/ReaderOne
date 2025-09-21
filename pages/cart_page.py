from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class CartPage(Base):
    # Locators
    name_product = '//tbody/tr/td[@class="cart-item-name"]'
    price_product = '//tbody/tr/td[@class="cart-item-price"]'
    checkout_button = '//input[@id="basketOrderButton2"]'


    # Getters
    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))



    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('checkout button click')

    # Methods
    def checkout_product(self):
        name_product = self.get_name_product().text.lower()
        price_product = self.get_price_product().text
        self.click_checkout_button()
        print('checkout product click')
        return name_product, price_product
