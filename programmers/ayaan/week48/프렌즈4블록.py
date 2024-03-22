def solution(m, n, board):
    answer = 0

    new_board = []
    for i in range(m):
        line = []
        for ch in board[i]:
            line.append(ch)
        new_board.append(line)

    while True:
        del_point = set()
        for i in range(m - 1):
            for j in range(n - 1):
                p = new_board[i][j]
                if p == '0':
                    continue
                if new_board[i + 1][j] == p and new_board[i][j + 1] == p and new_board[i + 1][j + 1] == p:
                    del_point.add((i, j))
                    del_point.add((i + 1, j))
                    del_point.add((i, j + 1))
                    del_point.add((i + 1, j + 1))

        if len(del_point) == 0:
            break
        answer += len(del_point)
        for i, j in del_point:
            new_board[i][j] = '0'

        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    p = new_board[i][j]
                    if p != '0' and new_board[i + 1][j] == '0':
                        new_board[i][j] = '0'
                        new_board[i + 1][j] = p
                        moved = 1
            if moved == 0:
                break

    return answer
