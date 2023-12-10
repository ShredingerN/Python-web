from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    # пути(локаторы) элементов страницы
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PSWD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_LOGIN_RESULT = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_CREATE_NEW_POST = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_POST_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_POST_DESCRIPTION = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_POST_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_SAVE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_EXIST_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_CONTACTUS_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_YOU_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOU_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACTUS_SEND_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f'Send {word} to element {element_name} ')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.info(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.info(f'We find text {text} in error field {element_name}')
        return text

    # enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description='login form')

    def enter_pswd(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PSWD_FIELD, word, description='pswd form')

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_POST_TITLE, word, description='title')

    def enter_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_POST_DESCRIPTION, word, description='description')

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_POST_CONTENT, word, description='content')

    def enter_name_field(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOU_NAME_FIELD, word, description='contact name')

    def enter_email_field(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOU_EMAIL_FIELD, word, description='contact mail')

    def enter_content_field(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT_FIELD, word, description='contact content')

    # click buttons
    def click_login_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_LOGIN_BTN, description='login')

    def click_new_post_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_CREATE_NEW_POST, description='new post')

    def click_save_new_post_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_SAVE_BTN, description='save post')

    def click_contactus_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_CONTACTUS_BTN, description='contact')

    def click_contactus_send_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_CONTACTUS_SEND_BTN, description='send')

    # get text
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD, description='error label')

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_LOGIN_RESULT, description='result')

    def check_exist_post(self):
        find_post = self.find_element(TestSearchLocators.LOCATOR_EXIST_POST, time=3)
        text = find_post.text
        logging.info(f'We find text {text} in login page {TestSearchLocators.LOCATOR_EXIST_POST[1]}')
        return self.get_text_from_element(TestSearchLocators.LOCATOR_EXIST_POST, description='exist post')

    def text_alert(self):
        logging.info('Get alert text')
        text = self.switch_to_alert()
        logging.info(text)
        return text
