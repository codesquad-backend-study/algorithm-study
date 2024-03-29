def solution(msg):
    d = {chr(64 + i): i for i in range(1, 27)}
    answer = []
    num = 27

    i = 0
    while i < len(msg):
        w = ''
        while True:
            w += msg[i]
            if i + 1 < len(msg):
                wc = w + msg[i + 1]
                if wc in d:
                    i += 1
                    continue
                else:
                    answer.append(d[w])
                    d[wc] = num
                    num += 1
                    break
            else:
                answer.append(d[w])
                break
        i += 1

    return answer
