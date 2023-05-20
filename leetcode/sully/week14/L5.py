class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        # 팰린드롬 판별 및 투포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        # 슬라이싱 우측으로 이동
        result = ''
        for i in range(len(s) - 1):
            # expand 각각 홀수, 짝수
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result