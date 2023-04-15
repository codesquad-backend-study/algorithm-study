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
        
        u_temp = u[1:-2]
        for ch in u_temp:
            u = ""
            if ch == "(":
                u += ")"
            else:
                u += "("
        result += u
    
    return result

def check_right_str(s):
    stack = []
    if len(s) != 0:
        stack.append(s[0])
    
    for i in range(1, len(s)):
        if len(stack) == 0 or stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    return False

print(solution("()))((()"))