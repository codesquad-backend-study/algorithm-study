import collections


class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses_map = collections.defaultdict(str)
        # parentheses_map['('] = ')'
        # parentheses_map['{'] = '}'
        # parentheses_map['['] = ']'

        # i = 0
        # while i < len(s) - 1:
        #     if parentheses_map[s[i]] == s[i + 1]:
        #         i += 2
        #         continue
        #
        #     return False
        #
        # return True
        # 위처럼하면 "{[]}"와 같은 케이스에서 걸러짐 -> 즉 스택 써야 하는 문제

        parentheses_map = collections.defaultdict(str)
        parentheses_map[')'] = '('
        parentheses_map['}'] = '{'
        parentheses_map[']'] = '['

        stack = []
        for each in s:
            # and를 쓰면 왼쪽 연산에서 틀릴 시 오른쪽은 안 보기 때문에 이렇게 써도 무방함
            if stack and parentheses_map[each] == stack[-1]:
                stack.pop()
                continue

            stack.append(each)

        if stack:
            return False

        return True
