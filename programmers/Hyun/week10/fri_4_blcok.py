def mask(sx, sy, columns, check):
    if columns[sx][sy] == '0':
        return

    if columns[sx][sy] == columns[sx + 1][sy] == columns[sx][sy + 1] == columns[sx + 1][sy + 1]:
        check[sx][sy] = check[sx + 1][sy] = check[sx][sy + 1] = check[sx + 1][sy + 1] = True
        global delete_flag
        delete_flag = True


def solution(m, n, board):
    columns = [[] for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    for blocks in board:
        for idx, block in enumerate(blocks):
            columns[idx].append(block)

    delete_flag = False
    ans = 0

    for y in range(m - 1):
        for x in range(n - 1):
            mask(x, y, columns, check)

    while delete_flag:
        delete_flag = False

        for y in range(m):
            for x in range(n):
                if check[x][y]:
                    ans += 1

        for x, column in enumerate(columns):
            erase_cnt = sum(check[x])
            column = [block for y, block in enumerate(column) if not check[x][y]]
            columns[x] = ['0'] * erase_cnt + column

        check = [[False] * m for _ in range(n)]

        for y in range(m - 1):
            for x in range(n - 1):
                mask(x, y, columns, check)

    print(ans)
    return ans