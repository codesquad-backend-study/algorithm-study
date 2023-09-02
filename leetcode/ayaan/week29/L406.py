import collections
import heapq


def reconstructQueue(people):
    hq = []
    for each in people:
        heapq.heappush(hq, (-each[0], each[1]))

    result = []
    while hq:
        each = heapq.heappop(hq)
        h, k = -each[0], each[1]

        result.insert(k, [h, k])
    print(result)
