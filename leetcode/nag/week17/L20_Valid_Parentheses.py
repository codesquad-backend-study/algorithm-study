class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char is ")" and stack[-1] is "(":
                stack.pop()
            elif char is "}" and stack[-1] is "{":
                stack.pop()
            elif char is "]" and stack[-1] is "[":
                stack.pop()
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False
        
