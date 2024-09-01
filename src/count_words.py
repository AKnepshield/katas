def count_words(words):
    words_list = []
    for word in words:
        words_list.append(word)
    word_count = len(words_list)
    return word_count


words = ["red", "black", "green"]
word_count = count_words(words)
print({word_count})


def count_words(words):
    return len(words)


words = ["red", "black", "green"]
word_count = count_words(words)
print(f"{word_count}")
