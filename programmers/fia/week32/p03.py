# 이모티콘 할인행사
from itertools import product


def solution(users, emoticons):
    # sales: 할인율 [10%, 20%, 30%, 40%]
    sales = [1, 2, 3, 4]

    # groups: 모든 경우의 수 찾기
    groups = product(sales, repeat=len(emoticons))

    # answer[0]: 플러스에 가입한 회원의 수
    # answer[1]: 이모티콘 판매 수익
    answer = [0, 0]

    for group in groups:
        cost = {1: 0, 2: 0, 3: 0, 4: 0}

        # 할인율별 판매 가능한 금액 구하기
        for sale, emoticon in zip(group, emoticons):
            cost[sale] += emoticon - (emoticon // 10) * sale

        # 누적 금액 구하기
        for i in range(len(sales)):
            cost[sales[i]] += sum([cost[sales[j]] for j in range(i + 1, len(sales))])

        joined_user = 0
        profit = 0

        # 사용자별 결과 계산하기
        for sale_limit, buy_max in users:
            sale_limit = max(10, sale_limit)

            sale_max = sale_limit // 10

            if sale_limit % 10 > 0:
                sale_max += 1

            if cost[sale_max] >= buy_max:
                joined_user += 1
            else:
                profit += cost[sale_max]

        # 결과 비교하기
        if answer[0] < joined_user:
            answer[0] = joined_user
            answer[1] = profit
        elif answer[0] == joined_user:
            answer[1] = max(answer[1], profit)

    return answer
