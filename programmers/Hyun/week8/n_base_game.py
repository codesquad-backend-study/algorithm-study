dic = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

def change(n, i):
    ans = ""

    if i == 0:
        return "0"

    while i > 0:
        if i % n in dic:
            ans += dic[i%n]
        else:
            ans += str(i%n)
        i //= n

    return ans[::-1]


def solution(n, t, m, p):
    word = ""
    ans = ""

    i = 0
    while len(word) < p-1 + (t * m):
        word += change(n, i)
        i+=1

    for i in range(t):
        ans += word[p-1 + i * m]

    return ans

# (p-1 + i * m) , i는 0부터 ~ t-1까지

# 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1,
# n -> 진수
# t -> 숫자개수
# m -> 사람수
# p -> 순서
