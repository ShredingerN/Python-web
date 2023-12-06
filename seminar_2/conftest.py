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


@pytest.fixture()
def site():
    my_site = Site(testdata['address'])
    yield  my_site
    my_site.close()

