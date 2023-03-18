import re

def solution(str1, str2):
    list1 = []
    list2 = []
    str1 = str1.upper()
    str1 = re.sub(r"[^A-Z]", " ", str1)
    str2 = str2.upper()
    str2 = re.sub(r"[^A-Z]", " ", str2)

    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        list1.append(tmp)

    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        list2.append(tmp)

    list1 = [s for s in list1 if ' ' not in s]
    list2 = [s for s in list2 if ' ' not in s]

    inter = [s for s in list1 if s in list2]
    union = list2+list1

    inter = len(inter)
    union = len(union) - inter
    jcard = (inter/union)*65536 if union != 0 else 65536

    return int(jcard)


print(solution('FRANCE','french'))