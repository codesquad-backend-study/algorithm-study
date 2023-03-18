import re
import math


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_dict = {}
    str2_dict = {}

    for i in range(len(str1) - 1):
        ch = str1[i: i + 2]
        if not ch[0].isalpha() or not ch[1].isalpha():
            continue

        if ch in str1_dict:
            str1_dict[ch] += 1
        else:
            str1_dict[ch] = 1

    for i in range(len(str2) - 1):
        ch = str2[i: i + 2]
        if not ch[0].isalpha() or not ch[1].isalpha():
            continue

        if ch in str2_dict:
            str2_dict[ch] += 1
        else:
            str2_dict[ch] = 1

    intersection = 0
    union = 0

    for ch1 in str1_dict:
        if ch1 in str2_dict:
            intersection += min(str2_dict[ch1], str1_dict[ch1])

    for ch1 in str1_dict:
        if ch1 not in str2_dict:
            union += str1_dict[ch1]

    for ch2 in str2_dict:
        if ch2 not in str1_dict:
            union += str2_dict[ch2]

    for ch1 in str1_dict:
        if ch1 in str2_dict:
            union += max(str1_dict[ch1], str2_dict[ch1])

    if union == 0:
        return 65536

    return math.floor(intersection / union * 65536)
