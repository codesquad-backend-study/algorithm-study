def solution(p):

    if correct(p) :
        return p

    answer = ''
    u = ''

    while p != '' :
        u += p[:2]
        p = p[2:]
        if correct(u) == False:
            u = u[1:-1]
            u.replace('(',')')
            u.replace(')','(')
            u = '('+u+')'
        answer += u
        u = ''
    return answer

def correct(p) :
    for i in range(len(p)//2) : # 올바른 괄호 문자열인지 확인
        p = p.replace('()','')
    if p == '' :
        return True
    return False
