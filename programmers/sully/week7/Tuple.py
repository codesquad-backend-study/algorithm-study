# "|" -> 합집합
# "-" -> 차집합


def solution(s):
    s = s.replace('{', '').replace('}', '')
    s_list = list(map(int, s.split(',')))
    s_dict = {}

    # count dict
    for i in s_list:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1

    # sort the dict by key
    return sorted(s_dict, key=lambda x: s_dict[x], reverse=True)

    # 폐기물 처리
    # s_array = s.split(r'},{')
    # s_array[0] = re.sub('[^,0-9]', '', s_array[0])
    # s_array[len(s_array) - 1] = re.sub('[^,0-9]', '', s_array[len(s_array) - 1])


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
