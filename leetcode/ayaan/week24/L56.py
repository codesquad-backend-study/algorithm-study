import heapq


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # heapq에 넣고 정렬
        interval_queue = []
        for interval in intervals:
            heapq.heappush(interval_queue, (interval[0], interval[1]))

        # 첫번째 값 hq에 넣고
        first = heapq.heappop(interval_queue)
        hq = [(first[0], first[1])]
        answer = []
        # interval_queue에서 하나씩 빼서 hq의 값과 비교해서 겹치면 병합해서 넣음
        while interval_queue:
            interval = heapq.heappop(interval_queue)

            if interval[0] <= hq[0][1]:
                node = heapq.heappop(hq)
                end = node[1] if node[1] > interval[1] else interval[1]
                heapq.heappush(hq, (node[0], end))
            else:
                # 겹치지 않으면 빼서 answer에 넣음
                answer.append(heapq.heappop(hq))
                heapq.heappush(hq, (interval[0], interval[1]))
        answer.append(heapq.heappop(hq))

        return answer
