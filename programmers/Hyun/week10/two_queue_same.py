import collections


def solution(queue1, queue2):
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)

    two_sum = sum(queue1) + sum(queue2)
    target = two_sum // 2

    if two_sum % 2 == 1:
        return -1

    max_value = max(queue1)
    max_value = max(queue2)

    if two_sum - max_value < max_value:
        return -1

    op_cnt = 0

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    cnt = 0
    max_count = len(queue1) * 3

    while queue1_sum != target:
        if queue1_sum > queue2_sum:
            q1 = queue1.popleft()
            queue2.append(q1)
            queue1_sum -= q1
            queue2_sum += q1


        else:
            q2 = queue2.popleft()
            queue1.append(q2)
            queue1_sum += q2
            queue2_sum -= q2

        op_cnt += 1

        cnt += 1
        if cnt > max_count:
            return -1

    return op_cnt
