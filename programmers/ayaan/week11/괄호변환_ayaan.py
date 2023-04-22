def solution(p):
    if len(p) == 0:
        return ""
    
    u = ""
    v = ""
    
    open_count = 0
    close_count = 0
    for i in range(len(p)):
        if p[i] == "(":
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            u = p[0:i+1]
            v = p[i+1:]
            break
    
    result = ""
    if check_right_str(u):
        result = u
        result += solution(v)
    else:
        result = "("
        result += solution(v)
        result += ")"
        
        u = u[1:-1]
        temp = ""
        for ch in u:
            if ch == "(":
                temp += ")"
            else:
                temp += "("
        result += temp
    
    return result

def check_right_str(s):
    stack = []
    
    for i in range(0, len(s)):
        if len(stack) == 0 and s[i] == ")":
            return False
        if len(stack) == 0 or stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    return False

print(solution("()))((()"))

# print(check_right_str("))(("))