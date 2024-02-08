def solution(board, moves):
    vertical = [[] for _ in range(len(board))]

    for row in range(len(board) - 1, -1, -1):
        for col in range(len(board)):
            if board[row][col] != 0:
                vertical[col].append(board[row][col])

    basket = []
    count = 0

    for move in moves:
        col = move - 1

        if vertical[col]:
            doll = vertical[col].pop()

            if basket and basket[-1] == doll:
                basket.pop()
                count += 2
            else:
                basket.append(doll)

    return count
