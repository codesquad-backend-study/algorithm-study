class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewels_map = {}

        for jewel in jewels:
            jewels_map[jewel] = 1

        for stone in stones:
            if stone in jewels_map:
                answer += 1

        return answer
