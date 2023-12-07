import yaml
from TestPage import OperationsHelper
import time
import random, string
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# копируем пути поле логина и пароля, вводим невалидные данные
def test_step1(browser):
    logging.info('Test 1 start')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pswd('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


# css_selector = 'span.mdc-text-field__ripple'
# # указываем режим, сам слектор, и какое свойство из этого взять
# print(site.get_element_property('css', css_selector, 'height'))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))

def test_step2(site, login_xpath, pswd_xpath, btn_xpath, result_success):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys(testdata['password'])
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    login = site.find_element('xpath', result_success)
    assert login.text == 'Blog'


# ДЗ№2
def test_step3(site, login_xpath, pswd_xpath, btn_xpath, btn_create_post,
               btn_save_post, tittle_post_xpath, description_post_xpath,
               content_post_xpath, tittle_save_post):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys(testdata['password'])
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    time.sleep(testdata['sleep_time'])
    btn_create = site.find_element('xpath', btn_create_post)
    btn_create.click()
    time.sleep(testdata['sleep_time'])
    input1 = site.find_element('xpath', tittle_post_xpath)
    input1.send_keys('I want drink!')
    input2 = site.find_element('xpath', description_post_xpath)
    input2.send_keys('Vodka')
    input2 = site.find_element('xpath', content_post_xpath)
    input2.send_keys("".join(random.choices(string.ascii_lowercase + string.digits, k=300)))
    btn_post = site.find_element('xpath', btn_save_post)
    btn_post.click()
    time.sleep(testdata['sleep_time'])
    result = site.find_element('xpath', tittle_save_post)
    assert result.text == 'I want drink!'
