def solution(n, build_frame):
    blue_print = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]

    def is_valid():
        for i in range(1, n + 1):
            for j in range(n + 1):
                if blue_print[i][j][0]:  # 해당 위치에 기둥이 있는 경우
                    if not blue_print[i - 1][j][0]:  # 아래에 기둥이 없는 경우
                        if not blue_print[i][j][1]:  # 보가 없는 경우
                            if j - 1 < 0 or not blue_print[i][j - 1][1]:  # 왼쪽 보가 없는 경우
                                return False

                if blue_print[i][j][1]:  # 해당 위치에 보가 있는 경우
                    # 아래에 기둥이 없으며, 오른쪽 아래에 기둥이 없으며, 양옆에 보가 없는 경우 유효하지 않다
                    if not blue_print[i - 1][j][0]:  # 아래에 기둥이 없는 경우
                        if not blue_print[i - 1][j + 1][0]:  # 오른쪽 아래에 기둥이 없는 경우
                            if j - 1 < 0 or not blue_print[i][j - 1][1] or not blue_print[i][j + 1][1]:  # 양옆에 보가 없는 경우
                                return False

        return True

    for x, y, a, b in build_frame:
        if b == 1:  # 설치하는 경우
            blue_print[y][x][a] = True

            if not is_valid():
                blue_print[y][x][a] = False

        elif b == 0:  # 제거하는 경우
            blue_print[y][x][a] = False

            if not is_valid():
                blue_print[y][x][a] = True

    structure = []

    for i, row in enumerate(blue_print):
        for j, col in enumerate(row):
            if col[0]:
                structure.append([j, i, 0])
            if col[1]:
                structure.append([j, i, 1])

    structure.sort()

    return structure
