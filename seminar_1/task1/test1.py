from task1 import check_word

def test_word(good_word, bad_word):
    assert  good_word in check_word(bad_word)