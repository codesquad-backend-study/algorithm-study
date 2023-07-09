def solution(expression):
    answer = []

    # 1. 숫자랑 특수문자 분리 (OK)
    i = 0
    es = []
    while len(expression) - 1 > i:
        if expression[i].isdigit():
            tmp = ''
            while expression[i].isdigit():
                tmp += str(expression[i])
                if len(expression) - 1 == i:
                    break
                i += 1

            es.append(tmp)
        else:
            es.append(expression[i])
            i += 1

    # 왜인지는 모르겠는데 이러한 경우가 있긴 하네
    if not es[-1].isdigit():
        es.append(expression[-1])

    # 2. 연산의 경우를 모두 계산한 후, 배열 answer에 저장해서 그 절댓값인 abs(max(배열))로 최댓값 찾기
    i = 0
    price = 0
    while i > len(expression):
        # 짝수일 경우: 숫자
        # 홀수일 경우: 연산
        # 그냥 이거 6가지 경우 다 써서 while문 5개 더 추가할까?
        # 그럼 이렇게 순서대로 하면 안 됨
        if i % 2 == 1:
            if expression[i] == '-':
                price += expression[i - 1] - expression[i + 1]
            elif expression[i] == '+':
                price += expression[i - 1] + expression[i + 1]
            elif expression[i] == '*':
                price += expression[i - 1] * expression[i + 1]

    answer.append(price)

    return abs(max(answer))


# result: 60420
print(solution("100-200*300-500+20"))
# result: 300
print(solution("50*6-3*2"))
