import collections


def solution(stones, k):
    result = []
    window = collections.deque()

    for i in range(k):
        while window and stones[window[-1]] < stones[i]:
            window.pop()

        window.append(i)
    result.append(stones[window[0]])

    for i in range(k, len(stones)):
        if window and window[0] < i - k + 1:
            window.popleft()

        while window and stones[window[-1]] < stones[i]:
            window.pop()

        window.append(i)

        result.append(stones[window[0]])

    return min(result)
