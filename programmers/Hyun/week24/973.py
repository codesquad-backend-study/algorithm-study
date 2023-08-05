class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for idx, each in enumerate(points):
            x = each[0]
            y = each[1]
            dist.append((x ** 2 + y ** 2, idx))

        dist.sort()

        ans = []
        for i in range(k):
            ans.append(points[dist[i][1]])
        return ans
