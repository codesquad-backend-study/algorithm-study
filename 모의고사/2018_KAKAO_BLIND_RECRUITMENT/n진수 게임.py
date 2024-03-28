# 0, 1, 2, ... 9, 1, 0, 1, 1, 1, 2
# n = 진법, t = 구할 숫자 갯수, m = 인원, p = 튜브 순서
# 튜브가 말해야 하는 숫자 t 개를 공백없이 차례로 나타내기

def convert(n, number, dictionary):
    a = []
    while number > 0:
        a.append(dictionary[number % n])
        number //= n
    a.reverse()
    if not a:
        return "0"
    return "".join(a)


def solution(n, t, m, p):
    dictionary = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D",
                  14: "E", 15: "F"}

    numbers = ""
    for i in range(n * t * m):
        numbers += convert(n, i, dictionary)

    ans = ""
    idx = p - 1
    while len(ans) < t:
        ans += numbers[idx]
        idx += m
    return ans
