EMPTY = 'EMPTY'


def solution(commands):
    board = [[EMPTY] * 50 for _ in range(50)]
    merged = [[(i, j) for i in range(50)] for j in range(50)]

    ans = []

    def merge(x1, y1, x2, y2):
        first_x, first_y = merged[y1][x1]
        second_x, second_y = merged[y2][x2]
        for i in range(50):
            for j in range(50):
                if merged[i][j] == (second_x, second_y):
                    merged[i][j] = (first_x, first_y)

        if board[first_y][first_x] == EMPTY and board[second_y][second_x] != EMPTY:
            board[first_y][first_x] = board[second_y][second_x]

    def update(x, y, value):
        sx, sy = merged[y][x]
        board[sy][sx] = value

    def change(old_value, new_value):
        for i in range(50):
            for j in range(50):
                if board[i][j] == old_value:
                    board[i][j] = new_value

    def unmerge(x, y):
        sx, sy = merged[y][x]
        tmp = board[sy][sx]

        for i in range(50):
            for j in range(50):
                if merged[i][j] == (sx, sy):
                    merged[i][j] = (j, i)
                    board[i][j] = EMPTY
        board[y][x] = tmp

    def print_board(x, y):
        sx, sy = merged[y][x]
        ans.append(board[sy][sx])

    for ins in commands:
        a = ins.split()

        if a[0] == 'UPDATE':
            if len(a) == 3:
                old = a[1]
                new = a[2]
                change(old, new)
            else:
                y = int(a[1]) - 1
                x = int(a[2]) - 1
                val = a[3]
                update(x, y, val)

        elif a[0] == 'MERGE':
            y1 = int(a[1]) - 1
            x1 = int(a[2]) - 1
            y2 = int(a[3]) - 1
            x2 = int(a[4]) - 1
            merge(x1, y1, x2, y2)

        elif a[0] == 'UNMERGE':
            y1 = int(a[1]) - 1
            x1 = int(a[2]) - 1
            unmerge(x1, y1)

        elif a[0] == 'PRINT':
            y1 = int(a[1]) - 1
            x1 = int(a[2]) - 1
            print_board(x1, y1)

    return ans
