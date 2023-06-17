class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dictionary = {}
        for j in jewels:
            dictionary[j] = True

        count = 0
        for s in stones:
            if s in dictionary:
                count += 1

        return count
