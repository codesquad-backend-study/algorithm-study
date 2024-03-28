def solution(n, t, m, p):

    mapper = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

    def change(n, value):
        result = ''

        q, r = divmod(n, value)

        while q > 0:
            result += mapper[r]
            q, r = divmod(q, value)

        result += mapper[r]

        return result[::-1]

    string = '0'
    max_index = (m * t) - (m - p)
    number = 1

    while len(string) < max_index:
        string += change(number, n)
        number += 1

    answer = ''
    for i in range(t):
        answer += string[p + (i * m) - 1]

    return answer
