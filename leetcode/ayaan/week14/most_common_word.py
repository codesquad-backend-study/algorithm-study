import re
import collections

def most_common_word(paragraph, banned):
    paragraph = re.sub("[^A-Za-z\s]", " ", paragraph).lower()

    word_list = paragraph.split()

    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)
    for word in banned:
        if word in word_count:
            word_count.pop(word)

    word_count = sorted(word_count.items(), key=lambda x : -x[1])
    print(word_count)

    return word_count[0][0]

most_common_word("Bob!", ["hit"])