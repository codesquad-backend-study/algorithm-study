def solution(board, skill):
    results = [[0] * len(board[0]) for _ in range(len(board))]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            results[r1][c1] -= degree
            if c2 + 1 < len(board[0]):
                results[r1][c2 + 1] += degree
            if r2 + 1 < len(board):
                results[r2 + 1][c1] += degree
            if r2 + 1 < len(board) and c2 + 1 < len(board[0]):
                results[r2 + 1][c2 + 1] -= degree
        else:
            results[r1][c1] += degree
            if c2 + 1 < len(board[0]):
                results[r1][c2 + 1] -= degree
            if r2 + 1 < len(board):
                results[r2 + 1][c1] -= degree
            if r2 + 1 < len(board) and c2 + 1 < len(board[0]):
                results[r2 + 1][c2 + 1] += degree

    for i in range(len(board)):
        for j in range(1, len(results[0])):
            results[i][j] += results[i][j - 1]

    for i in range(1, len(results)):
        for j in range(len(results[0])):
            results[i][j] += results[i - 1][j]

    count = 0
    for i in range(len(results)):
        for j in range(len(results[0])):
            board[i][j] += results[i][j]
            if board[i][j] > 0:
                count += 1

    return count
