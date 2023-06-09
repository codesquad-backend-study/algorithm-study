class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_brackets = {"(": 1, "{": 2, "[": 3}
        close_brackets = {")": 1, "}": 2, "]": 3}

        for ch in s:
            if ch in open_brackets:
                stack.append(open_brackets[ch])
            else:
                if not stack or stack[-1] != close_brackets[ch]:
                    return False

                stack.pop()

        return False if stack else True
