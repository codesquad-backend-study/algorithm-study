import collections


def removeDuplicateLetters(s: str):
    dictionary = collections.defaultdict(list)
    for index, alphabet in enumerate(s):
        dictionary[alphabet].append(index)
    results = sorted(dictionary.items(), key=lambda x: (x[0]))

    stack = []
    for word in results:
        pass


removeDuplicateLetters("cbacdcbc")
