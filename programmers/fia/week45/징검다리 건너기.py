from collections import deque


def solution(stones, k):
    max_queue = deque()

    def update_max(index):
        while max_queue and stones[max_queue[-1]] < stones[i]:
            max_queue.pop()

        max_queue.append(i)

    for i in range(k):
        update_max(i)

    answer = stones[max_queue[0]]

    for i in range(k, len(stones)):
        update_max(i)

        if max_queue[0] <= i - k:
            max_queue.popleft()

        answer = min(answer, stones[max_queue[0]])

    return answer
