from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0
        while i < len(g) and j < len(s):
            # 과자의 크기가 아이의 만족도보다 크거나 같다면 i 증가
            # 즉, 만족도가 가장 낮은 아이에게 크기가 가장 작은 과자를 주는 것
            if s[j] >= g[i]:
                i += 1

            # 과자를 어느 아이에게 주든 j는 무조건 증가
            j += 1

        return i
