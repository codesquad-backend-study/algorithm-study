from datetime import datetime

def solution(m, musicinfos):
    modified = {}
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    m = m.replace("A#", 'a')
    for element in musicinfos:
        temp = element.split(',')
        temp[3] = temp[3].replace("C#", 'c')
        temp[3] = temp[3].replace("D#", 'd')
        temp[3] = temp[3].replace("F#", 'f')
        temp[3] = temp[3].replace("G#", 'g')
        temp[3] = temp[3].replace("A#", 'a')
        hour = int(temp[1][:2]) - int(temp[0][:2])
        minutes = int(temp[1][3:]) - int(temp[0][3:])
        diff = hour * 60 + minutes
        length = len(temp[3])
        cord = temp[3] * (diff // length) + temp[3][:(diff % length)]
        modified[temp[2]] = cord
    answer = ''
    comparator = 0
    for key, value in modified.items():
        if m in value and comparator < len(value):
            answer = key
            comparator = len(value)
    if answer:
        return answer 
    else:
        return "(None)"
