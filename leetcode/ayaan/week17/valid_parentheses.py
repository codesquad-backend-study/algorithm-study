def isValid(s):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}

    for brace in s:
        if brace not in brackets:
            stack.append(brace)
        elif not stack or stack.pop() != brackets[brace]:
            return False

    return len(stack) == 0

print(isValid("([)]"))
