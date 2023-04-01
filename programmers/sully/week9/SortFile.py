def solution(files):
    tmp_answer = []

    # HEAD 구하자
    head_list = []
    for file in files:
        HEAD = ''
        for f in file:
            if f.isdigit():
                break
            else:
                HEAD += f

        # 아래처럼 한번에 하려 했는데 실패 그냥 따로따로 하기로 함
        # HEAD = ''
        # NUMBER = ''
        # HEAD_checked = False
        # NUMBER_checked = False
        # for f in file:
        #     if HEAD_checked is False:
        #         if f.isdigit():
        #             HEAD_checked = True
        #         else:
        #             HEAD += f
        #
        #     if NUMBER_checked is False:
        #         if f.isdigit() is False:
        #             NUMBER_checked = True
        #         else:
        #             NUMBER += f

        head_list.append(HEAD)

    # NUMBER 구하자
    number_list = []
    for i in range(len(files)):
        NUMBER = ''
        # 위에서 구해준 그 head_list의 마지막 문자 다음부터 해야지
        for j in range(len(head_list[i]), len(files[i])):
            if files[i][j].isdigit() is False:
                break
            else:
                NUMBER += files[i][j]

        number_list.append(NUMBER)

    # TAIL 구하자
    tail_list = []
    for i in range(len(files)):
        TAIL = ''

        # 위에서 구해준 head_list와 number_list의 size를 다 더한 것부터 시작해야지
        for j in range(len(head_list[i]) + len(number_list[i]), len(files[i])):
            TAIL += files[i][j]

        tail_list.append(TAIL)

    # (HEAD, NUMBER, TAIL)을 갖고 있는 튜플 2차원 리스트를 생성하자
    tuple_list = []
    for i in range(len(head_list)):
        my_tuple = (head_list[i], number_list[i], tail_list[i])
        tuple_list.append(my_tuple)

    # 각 HEAD를 기준으로 정렬하고 싶은데
    tmp_answer = sorted(tuple_list, key=lambda x: (x[0].upper(), int(x[1])))

    answer = []
    for i in range(len(tmp_answer)):
        answer.append(tmp_answer[i][0] + tmp_answer[i][1] + tmp_answer[i][2])

    return answer


# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
