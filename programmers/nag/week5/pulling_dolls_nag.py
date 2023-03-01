def solution(board, moves):
    result = 0
    basket = [0]
    for list in board:
        list.insert(0, 0)
    for move in moves:
        if board[-1][move] == 0:
            continue
        for i in range(len(board)):
            if board[i][move] != 0:
                if basket[-1] == board[i][move]:
                    basket.pop()
                    board[i][move] = 0
                    result += 2                    
                else:
                    basket.append(board[i][move])
                    board[i][move] = 0
                break
    return result
