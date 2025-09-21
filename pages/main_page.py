from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    # Locators
    catalog_button = '//td[@class="first item"]'

    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('click_catalog_button')

    # Methods
    def go_to_the_catalog(self):
        self.get_catalog_button().click()
        print('go_to_the_catalog')