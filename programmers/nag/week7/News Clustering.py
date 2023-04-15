import re

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    print(str1, str2)
    str1List = re.split(r'[\W_\d]', str1)
    str2List = re.split(r'[\W_\d]', str2)
    print(str1List)
    print(str2List)
    str1Set = []
    str2Set = []
    for string in str1List:
        if len(string) <= 1:
            continue
        for index in range(len(string) - 1):
            str1Set.append(string[index:index + 2])
    for string in str2List:
        if len(string) == 1:
            continue
        for index in range(len(string) - 1):
            str2Set.append(string[index:index + 2])
    union = []
    intersection = []
    for string in Str1Set:
        if string not in Str2Set:
            union.append(string)
        else:
            union.remove(string)
    print(str1Set)
    print(str2Set)
    
    print(union)
    print(intersection)
