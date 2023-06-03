def isValid(s):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if len(stack) == 0 and (ch == ")" or ch == "]" or ch == "}"):
            return False
        elif len(stack) == 0:
            stack.append(ch)
        else:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif stack[-1] != brackets[ch]:
                stack.append(ch)
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("([)]"))
