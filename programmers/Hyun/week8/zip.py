def solution(msg):
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}

    ans = []

    while len(msg) > 0:
        i = 0
        print(msg)

        j = i + 1
        while j <= len(msg) and msg[i:j + 1] in dic:
            j += 1

        word = msg[i:j]
        ans.append(dic[word])

        if j >= len(msg):
            break

        dic[msg[i:j + 1]] = len(dic) + 1

        msg = msg[j:]

    return ans