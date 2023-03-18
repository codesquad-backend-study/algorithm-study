def solution(n, k):
    count_answer = 0
    # 10진수(n) to k진법
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    number = tmp[::-1]

    # number(변환된 수)를 가지고 조건 비교
    # i + 1번째에서 0을 발견하면 0을 마지막으로 발견한 시점부터 i번째까지의 숫자를 가지고 비교 -> is_prime()
    tmp_i = ''
    is_zero = False
    for i in range(len(number)):
        tmp_i += number[i]
        if len(number) - 1 == i:
            if number[i - 1] == '0':
                is_zero = True
        else:
            if number[i + 1] == '0' or number[i - 1] == '0':
                is_zero = True

        if is_prime(int(tmp_i)) and is_zero:
            # 여기서 좌우 0인지 비교
            if '0' not in tmp_i:  # 여기서 101 같은 건 count 해주지 말기
                count_answer += 1
            tmp_i = ''

    return count_answer


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(solution(437674, 3))
print(solution(110011, 10))
