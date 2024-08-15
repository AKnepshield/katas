from src.count_words import count_words


def test_count_words_returns_zero():
    word_count = ""
    count_words_return = count_words(word_count)
    assert count_words_return == 0


def test_count_one_word():
    word_count = "word"
    count_words_return = count_words(word_count)
    assert count_words_return == 1


def test_count_two_words():
    word_count = "another word"
    count_words_return = count_words(word_count)
    assert count_words_return == 2
