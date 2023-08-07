import collections


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for index, point in enumerate(points):
            x, y = point[0], point[1]
            distance = ((x - 0) ** 2) + ((y - 0) ** 2)

            points[index] = (distance, point)

        points.sort()

        result = []

        for i in range(k):
            result.append(points[i][1])

        return result
