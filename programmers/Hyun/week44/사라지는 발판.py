EMPTY = 0
AVAILABLE = 1


def play(board, r1, c1, r2, c2):
    if board[r1][c1] == EMPTY:
        return False, 0
    board[r1][c1] = EMPTY
    R = len(board)
    C = len(board[0])
    min_win = float('inf')
    max_lose = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r1 + dr, c1 + dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == AVAILABLE:
            lose, count = play(board, r2, c2, nr, nc)
            if lose:
                max_lose = max(max_lose, count + 1)
            else:
                min_win = min(min_win, count + 1)
    board[r1][c1] = AVAILABLE
    if min_win < float('inf'):
        return True, min_win
    else:
        return False, max_lose


def solution(board, aloc, bloc):
    ar, ac = aloc
    br, bc = bloc
    _, ans = play(board, ar, ac, br, bc)
    return ans
