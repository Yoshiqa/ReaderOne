from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage(Base):
    # Locators
    name_product = '//td[@class="middletwo"]/div/h1'
    price_product = '(//div[@class="catalog-detail-price"]/p/span[@class="catalog-detail-price"])[1]'
    buy_button = '//td[@class="c63 catalog-detail-desc"]/div/div[4]/a'


    # Getters
    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))



    # Actions
    def click_buy_button(self):
        self.get_buy_button().click()
        print('click_buy_button')

    # Methods
    def buy_product(self):
        name_product = self.get_name_product().text.lower()
        price_product = self.get_price_product().text
        self.click_buy_button()
        print('buy_product')
        return name_product, price_product