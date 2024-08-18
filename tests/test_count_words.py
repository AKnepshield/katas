from src.count_words import count_words


def test_count_zero_words():
    string_of_words = ""
    string_list_int = count_words(string_of_words)
    assert string_list_int == 0


def test_count_one_words():
    string_of_words = "word"
    string_list_int = count_words(string_of_words)
    assert string_list_int == 1


def test_count_two_words():
    string_of_words = "two words"
    string_list_int = count_words(string_of_words)
    assert string_list_int == 2
