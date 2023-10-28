import collections


def solution(stones, k):
    answer = []
    max_value = collections.deque()

    for i in range(k):
        while max_value and stones[max_value[-1]] < stones[i]:
            max_value.pop()

        max_value.append(i)

    answer.append(stones[max_value[0]])

    for i in range(k, len(stones)):
        while max_value and max_value[0] < i - k + 1:
            max_value.popleft()

        while max_value and stones[max_value[-1]] < stones[i]:
            max_value.pop()

        max_value.append(i)
        answer.append(stones[max_value[0]])

    return min(answer)
