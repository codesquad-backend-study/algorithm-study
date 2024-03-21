def solution(m, n, board):
    answer = 0
    removed_set = set()

    for i in range(m):
        board[i] = list(board[i])

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if not board[i][j]:
                    continue

                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][
                    j + 1]:
                    removed_set.add((i, j))
                    removed_set.add((i, j + 1))
                    removed_set.add((i + 1, j))
                    removed_set.add((i + 1, j + 1))

        if removed_set:
            answer += len(removed_set)

            for i, j in removed_set:
                board[i][j] = []

            removed_set = set()
        else:
            return answer

        while True:
            moved = False
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and not board[i + 1][j]:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = True

            if moved is False:
                break
