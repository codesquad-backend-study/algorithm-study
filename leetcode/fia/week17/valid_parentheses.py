def isValid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
            continue
        if len(stack) == 0 and (bracket == ')' or bracket == '}' or bracket == ']'):
            return False
        if bracket == ')' and stack[-1] == '(':
            stack.pop()
            continue
        if bracket == '}' and stack[-1] == '{':
            stack.pop()
            continue
        if bracket == ']' and stack[-1] == '[':
            stack.pop()
            continue
        if bracket == ')' or bracket == '}' or bracket == ']':
            stack.append(bracket)

    return len(stack) == 0


print(isValid("(])"))
