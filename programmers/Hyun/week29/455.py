class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        ans = 0

        while g and s:
            if g[-1] <= s[-1]:
                ans += 1
                g.pop()

            s.pop()

        return ans
