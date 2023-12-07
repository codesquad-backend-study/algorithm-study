# x, y
# 0 기둥 |, 1 보 -
# 0 삭제, 1 설치
# 설치는 좌표에서 오른쪽으로
# 보는 기둥위에 있거나, 양쪽보위에 한번에 놓을 수 있어야 한다.
# 반환값은 x,y 좌표와 구조물 종류 (a=0=기둥, a=1=보)
# 모든 동작을 하고나서의 구조물을 반환

def solution(n, build_frame):
    def check():
        for y in range(1, n + 1):
            for x in range(n + 1):
                if x == 0:
                    if column_frame[y][x] == 1:
                        if column_frame[y - 1][x] == 0 and wall_frame[y][x] == 0:
                            return False

                    if wall_frame[y][x] == 1:
                        if column_frame[y - 1][x] == 0 and column_frame[y - 1][x + 1] == 0:
                            return False
                else:
                    if column_frame[y][x] == 1:
                        if column_frame[y - 1][x] == 0 and wall_frame[y][x - 1] == 0 and wall_frame[y][x] == 0:
                            return False

                    if wall_frame[y][x] == 1:
                        if column_frame[y - 1][x] == 0 and column_frame[y - 1][x + 1] == 0 and (
                                wall_frame[y][x - 1] == 0 or wall_frame[y][x + 1] == 0):
                            return False

        return True

    COLUMN = BREAK = 0
    WALL = CREATE = 1
    column_frame = [[0] * (n + 1) for _ in range(1000)]
    wall_frame = [[0] * (n + 1) for _ in range(1000)]

    for x, y, typ, build in build_frame:
        if build == CREATE:
            if typ == COLUMN:
                column_frame[y][x] = 1
                if not check():
                    column_frame[y][x] = 0
            else:
                wall_frame[y][x] = 1
                if not check():
                    wall_frame[y][x] = 0
        else:
            if typ == COLUMN:
                column_frame[y][x] = 0
                if not check():
                    column_frame[y][x] = 1
            else:
                wall_frame[y][x] = 0
                if not check():
                    wall_frame[y][x] = 1

    ans = []

    for y in range(1000):
        for x in range(n + 1):
            if column_frame[y][x] == 1:
                ans.append([x, y, COLUMN])

            if wall_frame[y][x] == 1:
                ans.append([x, y, WALL])
    ans.sort()

    return ans
