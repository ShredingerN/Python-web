from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocator:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PSWD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'send {word} to element {TestSearchLocator.LOCATOR_LOGIN_FIELD[1]}')
        # очистка поля
        login_field = self.find_element(TestSearchLocator.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pswd(self, word):
        logging.info(f'send {word} to element {TestSearchLocator.LOCATOR_PSWD_FIELD[1]}')
        # очистка поля
        login_field = self.find_element(TestSearchLocator.LOCATOR_PSWD_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click logging button')
        # находим кнопку
        self.find_element(TestSearchLocator.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocator.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocator.LOCATOR_ERROR_FIELD[1]}')
        return text
