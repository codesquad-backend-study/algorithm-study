class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0

        # n과 n - 1에 대하여 AND 연산을 진행 -> 무조건 비트가 1씩 제거됨
        # 즉, 이 연산을 진행한 횟수를 answer에 담으면 되는 문제
        while n != 0:
            n = n & (n - 1)
            answer += 1

        return answer
