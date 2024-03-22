import math


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    set1 = []
    set2 = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha():
            if str1[i + 1].isalpha():
                set1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha():
            if str2[i + 1].isalpha():
                set2.append(str2[i] + str2[i + 1])

    inter = 0
    copy = set2[:]
    for i in range(len(set1)):
        item = set1[i]
        for j in range(len(copy)):
            if item == copy[j]:
                inter += 1
                copy.remove(copy[j])
                break

    union = len(set1 + copy)
    if inter == 0 and union == 0:
        return 65536
    else:
        return math.floor(65536 * (inter / union))
