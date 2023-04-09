from collections import deque


def solution(queue1, queue2):  # len(queue1) == len(queue2)
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    # 2가 안 돼서 3으로.. ㅠ
    condition = len(queue1) * 3

    while True:
        if sum_q1 > sum_q2:
            target = queue1.popleft()
            queue2.append(target)

            sum_q1 -= target
            sum_q2 += target

            answer += 1
        elif sum_q1 < sum_q2:
            target = queue2.popleft()
            queue1.append(target)

            sum_q1 += target
            sum_q2 -= target

            answer += 1
        else:
            break

        if answer == condition:
            answer = -1
            break

    return answer


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

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
