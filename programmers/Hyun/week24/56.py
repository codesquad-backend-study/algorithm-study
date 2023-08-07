class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]

        ans = []
        for each in intervals[1:]:
            if each[0] <= end < each[1]:    # 연장
                end = each[1]

            elif end < each[0]:             # 단절
                ans.append((start, end))
                start = each[0]
                end = each[1]
                                            # 포함시에는 아무것도 x

        ans.append((start, end))
        return ans