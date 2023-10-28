import collections


def solution(gems):
    check = {}
    for gem in gems:
        check[gem] = 1

    kind = len(check)
    left = start = end = 0
    answer = []

    for right, gem in enumerate(gems, 1):
        kind -= check[gem] > 0
        check[gem] -= 1

        if kind == 0:
            while left < right and check[gems[left]] < 0:
                check[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right
                answer = [start + 1, end]

            check[gems[left]] += 1
            kind += 1
            left += 1

    return answer
