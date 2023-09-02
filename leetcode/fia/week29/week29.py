class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        count = 0

        while s and g:
            if g[-1] <= s[-1]:
                count += 1
                g.pop()
            s.pop()

        return count


