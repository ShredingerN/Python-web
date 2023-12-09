import pytest
from module import Site
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def login_xpath():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def pswd_xpath():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def btn_xpath():
    return '//*[@id="login"]/div[3]/button'


@pytest.fixture()
def result_xpath():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


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
