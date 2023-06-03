class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        dic = {}
        stack = []

        for ch in s:
            if ch in dic:
                for idx in range(len(stack)):
                    if ord(stack[idx]) < ord(ch):
                        stack.remove(ch)
                        break
            dic[ch] = 0
            stack.append(ch)

        return ''.join(stack)
