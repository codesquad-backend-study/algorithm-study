def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        deleted = set()

        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] != '-' and board[row][col] == board[row][col + 1]:  # 가로로 연속 2개가 같을 때
                    if board[row][col] == board[row + 1][col] and board[row + 1][col] == board[row + 1][col + 1]:  # 밑에 줄도 확인
                        # 2 x 2 형태로 4개가 붙어있는 경우
                        deleted.add((row, col))
                        deleted.add((row, col + 1))
                        deleted.add((row + 1, col))
                        deleted.add((row + 1, col + 1))

        if not deleted:
            break

        answer += len(deleted)

        for r, c in deleted:
            board[r][c] = "-"

        for col in range(n):
            for row in range(m - 2, -1, -1):

                while row + 1 < m and board[row + 1][col] == '-':
                    board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
                    row += 1

    return answer
