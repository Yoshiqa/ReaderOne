from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver


    """Method screenshot"""
    def get_screenshot(self):
        now_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.driver.save_screenshot(f'/Users/rushan/PycharmProjects/ReaderOne/screen/Screenshot{now_data}.png')


    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')
