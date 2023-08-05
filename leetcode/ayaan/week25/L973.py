import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i, point in enumerate(points):
            distance.append((i, (point[0] - 0) ** 2 + (point[1] - 0) ** 2))
        distance.sort(key=lambda x: x[1])

        answer = []
        for i in range(k):
            answer.append(points[distance[i][0]])

        return answer

    def kClosest_heapq(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for (x, y) in points:
            distance = (x - 0) ** 2 + (y - 0) ** 2
            heapq.heappush(hq, (distance, x, y))
        answer = []
        for _ in range(k):
            point = heapq.heappop(hq)
            answer.append([point[1], point[2]])
        return answer
