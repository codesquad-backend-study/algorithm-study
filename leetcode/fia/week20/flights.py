import collections
import heapq
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for start, to, price in flights:
        graph[start].append((price, to))  # 출발지 : (비용, 도착지)

    queue = [(0, src, 0)]  # (비용, 처음 출발지, 정류장 수)
    dictionary = collections.defaultdict(lambda: -1)
    print(graph)
    while queue:
        print(queue)
        price, destination, count = heapq.heappop(queue)
        dictionary[destination] = price
        if destination == dst:
            return dictionary[dst]
        print(dictionary)
        print(count)
        for p, d in graph[destination]:
            if count <= k:
                heapq.heappush(queue, (price + p, d, count + 1))

    return dictionary[dst]


print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
