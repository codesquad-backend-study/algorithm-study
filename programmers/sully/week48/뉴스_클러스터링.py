import math
from collections import Counter


def make_list(s):
    s_list = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i + 1].isalpha():
            s_list.append(s[i].lower() + s[i + 1].lower())
    return s_list


def solution(str1, str2):
    answer = 0

    str1_list = make_list(str1)
    str2_list = make_list(str2)

    hab = list((Counter(str1_list) | Counter(str2_list)).elements())
    gyo = list((Counter(str1_list) & Counter(str2_list)).elements())

    if len(hab) == 0:
        answer = 65536
    else:
        answer = math.trunc((len(gyo) / len(hab)) * 65536)

    return answer

