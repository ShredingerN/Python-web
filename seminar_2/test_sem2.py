import yaml
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata['address'])


# копируем пути поле логина и пароля, вводим невалидные данные
def test_step1(site, login_xpath, pswd_xpath, btn_xpath, result_xpath):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys('test')
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys('test')
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    err_label = site.find_element('xpath', result_xpath)
    assert err_label.text == '401'

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



