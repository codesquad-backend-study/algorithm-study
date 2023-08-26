class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0

        # xor로 만들어 주고
        xor_xy = x ^ y

        # 1의 개수를 찾으면 그게 바로 해밍 거리
        for each in bin(xor_xy):
            # bin으로 감싸면 string으로 처리가 됨
            if each == '1':
                answer += 1

        return answer


print(Solution().hammingDistance(1, 4))
