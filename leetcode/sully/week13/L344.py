from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ss = s.copy()
        for i in range(len(s)):
            s[len(ss) - 1 - i] = ss[i]


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
