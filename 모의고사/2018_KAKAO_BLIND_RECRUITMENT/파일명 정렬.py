# HEAD -> 문자로 이루어짐, 최소 한 글자 이상
# NUMBER -> 연속된 숫자로 이루어짐, 1 ~ 5글자, 앞쪽에 0 올 수 있음
# TAIL -> 숫자가 있을수도 있고, 걍 없을수도 있음,

# 1. HEAD 기준으로 사전순 정렬, 대소문자 구분 x
# 2. NUMBER 숫자순 정렬, 숫자 앞의 0은 무시
# 3. 원래 입력으로 주어진 순서 유지
def solution(files):
    f = []
    origins = []
    for idx, file in enumerate(files):
        head = ""
        number = ""
        tail = ""

        head_end = 0
        for i in range(len(file) - 1):
            if file[i + 1].isdigit():
                head_end = i + 1
                break
        head = file[:head_end]

        for i in range(head_end, head_end + 5):
            if i == len(file) - 1:
                number_end = i + 1
                break

            if not file[i + 1].isdigit():
                number_end = i + 1
                break

            number_end = i + 1
        number = file[head_end:number_end]

        origins.append(file)

        f.append((head.lower(), int(number), idx))

    f.sort()

    ans = []
    for _, _, idx in f:
        ans.append(origins[idx])
    return ans
