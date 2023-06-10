class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        jewel = set(c for c in jewels)
        answer = 0

        for c in stones:
            if c in jewel:
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
        for key in dict:
            answer += dict[key]
        return answer
