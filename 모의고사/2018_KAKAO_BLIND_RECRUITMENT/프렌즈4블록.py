# 2*2 가 같으면 블록을 지운다.
# 지워진 블록은 내려온다.
# 또 지워질 수 있다.
# 총 지워진 개수를 출력하라.

def mask(sx, sy, board):
    return (board[sy][sx] == board[sy][sx + 1] == board[sy + 1][sx] == board[sy + 1][sx + 1])


def solution(m, n, board):
    a = [[-1] * n for _ in range(m)]
    DELETED = -1

    for y in range(m):
        for x in range(n):
            a[y][x] = board[y][x]

    while True:
        # 2x2 를 만족하는 시작좌표 모으기
        deletable_start_points = []
        for y in range(m - 1):
            for x in range(n - 1):
                if a[y][x] != DELETED:
                    if mask(x, y, a):
                        deletable_start_points.append((x, y))

        # 2x2 를 만족하는 좌표들 지우기
        for x, y in deletable_start_points:
            a[y][x] = a[y][x + 1] = a[y + 1][x] = a[y + 1][x + 1] = DELETED

        # 지워진 부분들은 위로 올리고, 위에 있는 블록들은 내리기
        for x in range(n):
            d = []
            no_d = []
            for y in range(m):
                if a[y][x] == DELETED:
                    d.append(DELETED)
                else:
                    no_d.append(a[y][x])

            for y in range(len(d)):
                a[y][x] = DELETED
            for y in range(len(no_d)):
                a[y + len(d)][x] = no_d[y]

        # 만약 지워진 요소가 없다면 탈출
        if not deletable_start_points:
            break

    ans = 0
    for y in range(m):
        for x in range(n):
            if a[y][x] == DELETED:
                ans += 1

    return ans
