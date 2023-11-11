# [type(1 공격, 2 회복), 시작행, 시작열, 끝행, 끝열, 강도]

def solution(board, skill):
    summation = [[0] * len(board[0]) for _ in range(len(board))]

    for each in skill:
        sx, sy, ex, ey, point = each[2], each[1], each[4], each[3], each[5]
        if each[0] == 1:
            point = -point

        summation[sy][sx] += point

        if ex + 1 < len(board[0]):
            summation[sy][ex + 1] += -point

        if ey + 1 < len(board):
            summation[ey + 1][sx] += -point

        if ex + 1 < len(board[0]) and ey + 1 < len(board):
            summation[ey + 1][ex + 1] += point

    for y in range(len(board)):  # 가로 누적합
        for x in range(1, len(board[0])):
            summation[y][x] += summation[y][x - 1]

    for x in range(len(board[0])):  # 세로 누적합
        for y in range(1, len(board)):
            summation[y][x] += summation[y - 1][x]

    ans = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += summation[y][x]
            if board[y][x] > 0:
                ans += 1

    return ans
