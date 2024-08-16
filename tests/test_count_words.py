from src.count_words import count_words


def test_count_zero_words():
    empty_string = ""
    word_count = count_words(empty_string)
    assert word_count == 0


def test_count_one_word():
    single_word = "one"
    count_words_return = count_words(single_word)
    assert count_words_return == 1


def test_count_two_words():
    two_words = "two words"
    count_words_return = count_words(two_words)
    assert count_words_return == 2
