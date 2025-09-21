import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def set_up():
    print('Start test')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    service = Service(executable_path='/Users/rushan/PycharmProjects/Resource/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.readerone.ru/'
    driver.get(url)

    yield driver
    driver.quit()
    print('Finish test')