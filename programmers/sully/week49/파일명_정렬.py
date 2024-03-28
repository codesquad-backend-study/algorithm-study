from typing import List


def solution(files: List[str]) -> List[str]:
    head_list = []
    for file in files:
        HEAD = ''
        for f in file:
            if f.isdigit():
                break
            else:
                HEAD += f

        head_list.append(HEAD)

    number_list = []
    for i in range(len(files)):
        NUMBER = ''
        for j in range(len(head_list[i]), len(files[i])):
            if files[i][j].isdigit() is False:
                break
            else:
                NUMBER += files[i][j]

        number_list.append(NUMBER)

    tail_list = []
    for i in range(len(files)):
        TAIL = ''

        # 위에서 구해준 head_list와 number_list의 size를 다 더한 것부터 시작해야지
        for j in range(len(head_list[i]) + len(number_list[i]), len(files[i])):
            TAIL += files[i][j]

        tail_list.append(TAIL)

    tuple_list = []
    for i in range(len(head_list)):
        my_tuple = (head_list[i], number_list[i], tail_list[i])
        tuple_list.append(my_tuple)

    tmp_answer = sorted(tuple_list, key=lambda x: (x[0].upper(), int(x[1])))
    answer = []
    for i in range(len(tmp_answer)):
        answer.append(tmp_answer[i][0] + tmp_answer[i][1] + tmp_answer[i][2])

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
