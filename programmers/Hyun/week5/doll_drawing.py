def solution(board, moves):
    moves = [i - 1 for i in moves]
    bucket = []

    line = []

    for x in range(len(board[0])):
        tmp = []
        for y in range(len(board)):
            if board[y][x] == 0:
                continue
            else:
                tmp.append(board[y][x])
        line.append(tmp[::-1])

    ans = 0

    for move in moves:
        if line[move]:
            bucket.append(line[move].pop())
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            ans += 2
            bucket.pop()
            bucket.pop()

    return ans