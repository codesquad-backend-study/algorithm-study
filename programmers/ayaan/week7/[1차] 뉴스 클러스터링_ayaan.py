import re
import math

def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    li1 = []
    li2 = []
    
    for i in range(max(len(str1), len(str2)) - 1):
        if re.match("[A-Z]{2}", str1[i:i+2]):
            li1.append(str1[i:i+2])
        if re.match("[A-Z]{2}", str2[i:i+2]):
            li2.append(str2[i:i+2])
    
    intersection = 0
    union = 0
    
    li1_set = set(li1)
    for val in li1_set:
        if val in li2:
            intersection += 1
    
    li_set = set(li1 + li2)
    for val in li_set:
        union += max(li1.count(val), li2.count(val))
    
    if intersection == 0 and union == 0:
        return 65536
    else:
        return math.trunc(intersection / union * 65536)

print(solution("handshake", "shake hands"))