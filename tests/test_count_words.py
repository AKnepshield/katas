from src.count_words import count_words


def test_count_zero_words():
    word_count = ""
    string_int = count_words(word_count)
    assert string_int == 0


def test_count_one_word():
    word_count = "word"
    string_int = count_words(word_count)
    assert string_int == 1


def test_count_two_words():
    word_count = "two words"
    string_int = count_words(word_count)
    assert string_int == 2
