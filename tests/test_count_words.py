from src.count_words import count_words


def test_count_words_returns_zero():
    word_count = ""
    word_count_return = count_words(word_count)
    assert word_count_return == 0


def test_count_words_returns_one():
    word_count = "one"
    word_count_return = count_words(word_count)
    assert word_count_return == 1


def test_count_words_returns_two():
    word_count = "two words"
    word_count_return = count_words(word_count)
    assert word_count_return == 2
