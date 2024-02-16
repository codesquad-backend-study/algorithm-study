import collections


def solution(gems):
    answer = []
    kind = len(set(gems))
    start, end = 0, 0
    gem_dict = collections.defaultdict(int)

    while True:
        if start == len(gems):
            break
        if len(gem_dict) == kind:
            answer.append((start, end))
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
            continue
        if end == len(gems):
            break
        if len(gem_dict) != kind:
            gem_dict[gems[end]] += 1
            end += 1
            continue

    length = float('inf')
    result = []
    for s, e in answer:
        if length > e - s:
            length = e - s
            result = [s + 1, e]

    return result
