from collections import deque


def solution(queue1, queue2):  # len(queue1) == len(queue2)
    count_case1 = 0
    count_case2 = 0

    # 방법 구하는 메인 로직
    # 방법 1. q2의 마지막 전까지 pop.left -> q1 append, q1의 앞 로직에서 추가되기 전까지 pop.left -> q2 append
    q1, q2 = deque(queue1), deque(queue2)
    while True:
        q1_len = len(q1)
        for _ in range(len(q2) - 1):
            q1.append(q2.popleft())
        count_case1 += 1
        if sum(q1) == sum(q2):
            break

        for _ in range(q1_len):
            q2.append(q1.popleft())
        count_case1 += 1
        if sum(q1) == sum(q2):
            break

    # 방법 2. q1 pop.left -> q2 append, q2 pop.left -> q1 append
    q1, q2 = deque(queue1), deque(queue2)
    while True:
        q2.append(q1.popleft())
        # 둘의 sum이 같으면 break하기 (이미 카운트는 증가한 상태니까 신경 ㄴㄴ)
        # 반복문 돌 떄마다 방법 2의 카운트 1씩 증가
        count_case2 += 1
        if sum(q1) == sum(q2):
            break

        # 이렇게 작업은 2번 해야 되는 거임
        q1.append(q2.popleft())
        count_case2 += 1
        if sum(q1) == sum(q2):
            break

    print(count_case1)
    print(count_case2)
    # min() 함수를 이용하여 아래의 방법 중 최소인 것을 구하기
    answer = min(count_case2, count_case1)

    # 만약 구할 수 없는 경우 answer에 -1 저장
    # 이 경우는 while True문에 걸려서 못 빠져 나오고 반복 루프가 되는 경우일 텐데 어떻게 판단해야 할까
    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))

# 테스트 결론: popleft()후 변수에 저장하면 원본 값에도 결국 popleft가 됨
# # @Test
# d = deque()
# d.append(1)
# d.append(2)
# d.append(3)
#
# print(d)
# L = d.popleft()
# print(d)
