from typing import List


class Solution:
    # 조합 문제니 순서 고려 X
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        # '1'이랑 '0'은 만들어줄 필요가 없음 (예외 처리 안 해줘도 되도록 문제에서 제시)
        digits_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # (0 <= digits.length <= 4) -> 재귀로 푸는 게 더 효과적일 듯
        def dfs(index: int, element: str) -> None:
            # 끝까지 탐색 -> 백트래킹
            if len(digits) == len(element):
                answer.append(element)
                return

            for i in range(index, len(digits)):
                # 한 자리수의 숫자(ex. digits_map['2'])에 대한 string(ex. 'abc')
                for c in digits_map[digits[i]]:
                    print(element + c)
                    dfs(i + 1, element + c)

        if not digits:
            return []

        dfs(0, '')

        return answer
