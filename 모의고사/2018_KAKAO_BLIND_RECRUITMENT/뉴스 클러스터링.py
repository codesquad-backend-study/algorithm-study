# 자카드 유사도 = 교집합 크기 / 합집합 크기
# 둘다 공집합일땐 1
# 두글자씩 끊어 다중집합 원소로 만든다.
# 특수 문자, 공백, 숫자가 들어있는 원소쌍은 버린다.
# 대소문자는 구별하지 않는다.

def split(s):
    splited = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i + 1].isalpha():
            splited.append(s[i:i + 2])
    return splited


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    a = split(str1)
    b = split(str2)

    if len(a) < len(b):
        a, b = b, a

    j = 0
    J = 0
    for each in a:
        if each in b:
            b.remove(each)
            j += 1
        J += 1
    J += len(b)

    if j == J and j == 0:
        return 65536
    else:
        return int(j / J * 65536)
