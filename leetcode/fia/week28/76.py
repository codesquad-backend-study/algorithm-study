import collections


def minWindow(s: str, t: str) -> str:
    counter = collections.Counter(t)
    alphabets = set(list(t))
    has = []
    results = []
    dictionary = collections.defaultdict(collections.deque)

    for i, char in enumerate(s):
        if char in alphabets:  # 아직 필요한 char를 모두 찾지 못했는데 중복된 char를 발견한 경우
            if len(dictionary[char]) == counter[char]:
                dictionary[char].popleft()
            else:
                has.append(char)
            dictionary[char].append(i)
        if len(has) == len(t):
            indexes = []
            for value in dictionary.values():
                for index in value:
                    indexes.append(index)
            results.append(s[min(indexes):max(indexes) + 1])

    return min(results, key=len)


print(minWindow("aa", "aa"))
