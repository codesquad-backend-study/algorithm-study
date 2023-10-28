def solution(gems):
    kind = {}
    for gem in gems:
        kind[gem] = 1

    left = start = end = 0
    missing = len(kind)

    for right, gem in enumerate(gems, 1):
        missing -= kind[gem] > 0
        kind[gem] -= 1

        if missing == 0:
            while kind[gems[left]] < 0:
                kind[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right

            kind[gems[left]] += 1
            missing += 1
            left += 1

    return start + 1, end
