class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = {ch: 1 for ch in jewels}

        ans = 0
        for ch in stones:
            if ch in jewel:
                ans += 1

        return ans
