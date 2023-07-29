class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]

            if results[-1][1] >= start:
                results[-1][1] = max(results[-1][1], end)
                continue

            results.append(interval)

        return results
