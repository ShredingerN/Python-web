from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# реализация класса работы с веб-страницей, открытие, поиск элемента и определение его свойств

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    # настроили явное ожидание
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Сant find element by {locator}')

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)
