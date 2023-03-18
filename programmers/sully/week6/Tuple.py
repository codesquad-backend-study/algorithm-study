# "|" -> 합집합
# "-" -> 차집합

import re


def solution(s):
    # s -> set형 집합
    # 아 string형이구나..
    answer = []
    # 정규식으로 "},{"를 기준으로 {숫자} 형태의 2차원 배열 만들어보자
    # 앞, 뒤의 {{와 }}만 제거 후 int형 2차원 리스트로 매핑
    s_array = s.split(r'},{')
    s_array[0] = re.sub('[^,0-9]', '', s_array[0])
    s_array[len(s_array) - 1] = re.sub('[^,0-9]', '', s_array[len(s_array) - 1])
    print(s_array)
    # 2차원 배열을 for문을 돌면서 각각의 ","를 기준 -> int형 리스트로 매핑
    # 2차원 배열이니 [s for~ for] 사용
    s_to_int_array = []
    # for frame in range(s_array):
    #     s_to_int_array.append(frame)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
