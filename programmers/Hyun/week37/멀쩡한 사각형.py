def solution(w, h):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    n = gcd(w, h)
    w1 = w // n
    h1 = h // n

    blank = (h1 + w1 - 1) * (w // w1)
    return w * h - blank
