def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        doll = 0
        for i in range(len(board)):
            a = board[i][move - 1]
            if a != 0:
                board[i][move - 1] = 0
                doll = a
                break
        if doll == 0:
            continue

        if stack and stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)
    return answer
