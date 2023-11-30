import math


def solution(w: int, h: int) -> int:
    gcd = math.gcd(w, h)
    ww, hh = w // gcd, h // gcd

    each = ww + hh - 1
    print(each)

    return w * h - each * (w // ww)


print(solution(8, 12))
