# 조합 개념을 이용하는 거니 한번 내장함수 써보자
# 그럼 자동으로 조합이 저장되니까
from itertools import combinations


def solution(orders, course):  # orders: 단품 메뉴가 문자열 형식으로 담김, course: 새로 추가하게 될 메뉴가 담김
    answer = []
    set_answer = set()

    for order in orders:
        tuple_list = []
        # 자동으로 조합 생성
        for c in course:
            # 요리 c개 코스의 조합
            # 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return
            tmp = sorted(combinations(order, c))

            # 각 튜플을 문자열로 합치기 (join이었나)
            for t in tmp:
                tuple_list.append(''.join(t))

        gyo = set(tuple_list) & set(orders)
        for g in gyo:
            set_answer.add(g)

    l = list(set_answer)
    answer = sorted(l)
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
