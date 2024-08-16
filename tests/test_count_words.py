from src.count_words import count_words


def test_count_zero_words():
    word_count = ""
    word_count_return = count_words(word_count)
    assert word_count_return == 0


def test_count_one_word():
    word_count = "one"
    word_count_return = count_words(word_count)
    assert word_count_return == 1


def test_count_two_words():
    word_count = "one two"
    word_count_return = count_words(word_count)
    assert word_count_return == 2
