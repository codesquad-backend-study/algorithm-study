def solution(today, terms, privacies):
    answer = []
    termsModified = {}
    privaciesModified = []
    today = dateToDays(today) 
    for string in terms:
        splitString = string.split()
        termsModified[splitString[0]] = int(splitString[1])
    for string in privacies:
        splitString = string.split()   
        splitString[0] = dateToDays(splitString[0])
        privaciesModified.append(splitString)
    for i in range(len(privaciesModified)):
        privaciesModified[i][0] += termsModified[privaciesModified[i][1]] * 28 - 1
        if privaciesModified[i][0] < today:
            answer.append(i+1)
    return answer


def dateToDays(date):
    dateSplit = date.split('.')
    for i in range(len(dateSplit)):
        dateSplit[i] = int(dateSplit[i])
    return dateSplit[0] * 12 * 28 + dateSplit[1] * 28 + dateSplit[2]
