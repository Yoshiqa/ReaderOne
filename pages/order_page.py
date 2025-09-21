from datetime import datetime, timedelta

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class OrderPage(Base):
    # Locators
    city = '//div[@class="dropdown-block bx-ui-sls-input-block"]/div/input[@value="2941"]'
    dropdown_city = '//div[@class="bx-ui-sls-variants"]'
    individual_button = '//input[@id="PERSON_TYPE_1"]'
    pickup_button = '//input[@id="ID_DELIVERY_ID_2"]'
    lastname = '//input[@id="ORDER_PROP_1"]'
    name = '//input[@id="ORDER_PROP_34"]'
    email = '//input[@id="ORDER_PROP_2"]'
    mobile_code = '//input[@id="ORDER_PROP_64"]'
    mobile_number = '//input[@id="ORDER_PROP_3"]'
    date_of_receipt = '//input[@id="ORDER_PROP_33"]'
    time_of_receipt_from_10_to_15_checkbox = '//input[@id="ORDER_PROP_68[]_0"]'
    cash_button = '//input[@id="ID_PAY_SYSTEM_ID_1"]'
    name_product = '//tbody/tr/td[@class="cart-item-name"]'
    price_product = '//tbody/tr/td[@class="cart-item-price"]'
    login = '//td[@class="prop-value"]/input[@id="USER_LOGIN"]'
    agree_checkbox = '//input[@id="iblock_agree"]'
    loader = '//div[@id="wait_order_form_div_order_form_div"]'


    # Getters
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_dropdown_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_city)))

    def get_individual_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.individual_button)))

    def get_pickup_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_button)))

    def get_lastname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lastname)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_mobile_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_code)))

    def get_mobile_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number)))

    def get_date_of_receipt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_of_receipt)))

    def get_time_of_receipt_from_10_to_15_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.time_of_receipt_from_10_to_15_checkbox)))

    def get_cash_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cash_button)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_agree_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_checkbox)))



    # Actions
    def input_city(self, city):
        self.get_city().click()
        self.get_city().clear()
        self.get_city().send_keys(city)
        self.get_city().send_keys(Keys.SPACE)
        # Пришлось добавить Keys.SPACE чтобы вызвать событие и отобразился выпдающий список. Через execute_script или
        # ввод по символам - не работал.
        print('input city success')

    def wait_and_click_dropdown(self):
        self.get_dropdown_city().click()
        print('select city success')

    def click_individual_button(self):
        self.get_individual_button().click()
        print('input individual button success')

    def click_pickup_button(self):
        self.get_pickup_button().click()
        print('input pickup button success')

    def input_lastname(self, lastname):
        self.get_lastname().send_keys(lastname)
        print('input lastname success')

    def input_name(self, name):
        self.get_name().send_keys(name)
        print('input name success')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('input email success')

    def input_mobile_code(self, mobile_code):
        self.get_mobile_code().send_keys(mobile_code)
        print('input mobile code success')

    def input_mobile_number(self, mobile_number):
        self.get_mobile_number().send_keys(mobile_number)
        print('input mobile number success')

    def input_date_of_receipt(self, date_of_receipt):
        self.get_date_of_receipt().click()
        self.get_date_of_receipt().clear()
        self.get_date_of_receipt().send_keys(date_of_receipt)
        print('input date_of_receipt success')

    def click_time_of_receipt_from_10_to_15_checkbox(self):
        self.get_time_of_receipt_from_10_to_15_checkbox().click()
        print('input time_of_receipt_from_10_to_15_checkbox success')

    def click_cash_button(self):
        self.get_cash_button().click()
        print('input cash_button success')

    def input_login(self, login):
        self.get_login().send_keys(login)
        print('input login success')

    def click_agree_checkbox(self):
        self.get_agree_checkbox().click()
        print('input agree_checkbox success')

    def wait_invisibility_loader(self):
        try:
            if self.driver.find_element(By.XPATH, self.loader):
                WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
                print('loader disappeared or invisibility success')
        except TimeoutException:
            print('loader did"n disappear in time')
            self.get_screenshot()

    # Methods
    def place_an_order(self):
        self.input_city('Москва')
        self.wait_and_click_dropdown()
        self.wait_invisibility_loader()
        self.click_individual_button()
        self.wait_invisibility_loader()
        self.click_pickup_button()
        self.wait_invisibility_loader()
        self.input_lastname('Ivanov')
        self.input_name('Ivan')
        self.input_email('Ivanov@gmail.com')
        self.input_mobile_code('999')
        self.input_mobile_number('9999999')
        self.click_time_of_receipt_from_10_to_15_checkbox()
        self.click_cash_button()
        self.wait_invisibility_loader()
        self.input_date_of_receipt(f'{(datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')}')
        self.input_login('Ivanov')
        self.click_agree_checkbox()
        self.assert_url('https://www.readerone.ru/personal/order/make/')
        self.get_screenshot()
        name_product = self.get_name_product().text.lower()
        price_product = self.get_price_product().text
        print('place an_order success')
        return name_product, price_product