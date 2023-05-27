import re
import collections

def most_common_word(paragraph, banned):
    paragraph = re.sub(r"[^A-Za-z\s]", " ", paragraph).lower()

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

def most_common_word2(paragraph, banned):
    words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
             if word not in banned]

    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # return max(counts, key=counts.get)
    counts = collections.Counter(words)
    print(counts.most_common(1))
    s = "anagrams"
    print("".join(sorted(s)))
    return counts.most_common(1)[0][0]

# most_common_word("Bob!", ["hit"])
print(most_common_word2("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
