from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    group1 = []
    group2 = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            group1.append((str1[i], str1[i + 1]))

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            group2.append((str2[i], str2[i + 1]))

    if not group1 and not group2:
        return 65536

    union = 0
    intersection = 0
    keys = set(group1 + group2)
    counter1 = Counter(group1)
    counter2 = Counter(group2)

    for key in keys:
        count1 = counter1[key] if key in counter1 else 0
        count2 = counter2[key] if key in counter2 else 0
        union += max(count1, count2)

        if count1 > 0 and count2 > 0:
            intersection += min(count1, count2)

    return int(intersection / union * 65536)
