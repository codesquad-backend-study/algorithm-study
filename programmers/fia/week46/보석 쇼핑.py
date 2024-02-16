from collections import Counter


def solution(gems):
    counter = Counter(gems)
    total = len(counter)
    left = 0
    right = 0
    required = {gem: 1 for gem in counter.keys()}

    answer = [1, len(gems)]
    minimum = len(gems)

    while left < len(gems) and right < len(gems):
        while total > 0 and right < len(gems):
            gem = gems[right]
            total -= required[gem] > 0
            required[gem] -= 1
            right += 1

        while required[gems[left]] < 0:
            required[gems[left]] += 1
            left += 1

        if total == 0 and minimum > (right - left):
            answer = [left + 1, right]
            minimum = right - left

        total += required[gems[left]] >= 0
        required[gems[left]] += 1
        left += 1

    return answer
