def solution(s):
    s = s.replace('{{', '').replace('}}', '')
    s = s.split('},{')

    s.sort(key=len)
    answer = [int(s[0])]
    for val in s[1:]:
        val = val.split(',')
        for num in val:
            num = int(num)
            if num not in answer:
                answer.append(num)
                break

    return answer


solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
