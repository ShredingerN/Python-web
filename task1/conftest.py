import pytest

@pytest.fixture()
def good_word():
    return 'лошадь'

@pytest.fixture()
def bad_word():
    return 'лашадь'