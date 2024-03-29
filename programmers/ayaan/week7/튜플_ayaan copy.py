def solution(s):
    # "{" 와 "}"를 제거하고 리스트로 만든다.
    s = s.replace("{", "").replace("}", "")
    numList = s.split(",")
    
    countDict = {}
    # 숫자를 key, 개수를 value로 가지는 딕셔너리를 만든다.
    for num in numList:
        if num in countDict:
            countDict[num] += 1
        else:
            countDict[num] = 1
    
    # 딕셔너리를 value의 내림차순으로 정렬하고 key를 리스트로 만든다.
    # countDict = sorted(countDict.items(), key = lambda item: item[1], reverse = True)
    countDict = sorted(countDict.items(), key = lambda item: -item[1])
    result = [int(key) for key, value in countDict]
    
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))