import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# была одна инициализация для одного браузера в конфиге
# service = Service(testdata['driver_path'])


# получаем свойства элементов
# фикстура действует всю сессию
@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        # инициаоизация firefox
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    # инициаоизация chrome
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# @pytest.fixture()
# def login_xpath():
#     return '//*[@id="login"]/div[1]/label/input'


# @pytest.fixture()
# def pswd_xpath():
#     return '//*[@id="login"]/div[2]/label/input'


# @pytest.fixture()
# def btn_xpath():
#     return '//*[@id="login"]/div[3]/button'


# @pytest.fixture()
# def result_xpath():
#     return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def result_success():
    return '//*[@id="app"]/main/div/div[1]/h1'


# ДЗ№2
@pytest.fixture()
def btn_create_post():
    return '//*[@id="create-btn"]'


# ДЗ№2
@pytest.fixture()
def tittle_post_xpath():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


# ДЗ№2
@pytest.fixture()
def description_post_xpath():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


# ДЗ№2
@pytest.fixture()
def content_post_xpath():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


# ДЗ№2
@pytest.fixture()
def btn_save_post():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/span'


# ДЗ№2
@pytest.fixture()
def tittle_save_post():
    return '//*[@id="app"]/main/div/div[1]/h1'


@pytest.fixture()
def site():
    my_site = Site(testdata['address'])
    yield my_site
    my_site.close()
