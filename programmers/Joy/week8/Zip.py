def solution(msg):
    answer = []
    dic = { chr(65+i):i+1 for i in range(0,26)} # 'A':1
    mssg = msg

    while mssg :
        i = 0
        txt = mssg[i]
        while dic.get(txt) :
            i += 1
            txt = mssg[:i+1]

        dic[txt] = len(dic)+1
        txt = txt[:-1]
        answer.append(dic[txt])
        mssg = mssg[i:]

        if len(mssg) == 1:
            answer.append(dic[mssg])
            mssg = None

    return answer

print(solution('KAKAO'))