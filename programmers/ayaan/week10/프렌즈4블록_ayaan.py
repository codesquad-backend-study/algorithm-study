def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    answer = 0
    
    flag = True
    while(flag):
        flag = clear_block(m, n, board)
       
    return answer

def clear_block(m, n, board):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    clear_result = []
    for i in range(m-1):
        for j in range(n):
            block = board[i][j]
            clear_memory = [str(i) + str(j)]
            clear = False
            count = 0
            for k in range(3):
                # 옆칸으로 벗어나면 break
                if j+dy[k] >= n:
                    break
                # 다른 블록이면 break
                if block != board[i+dx[k]][j+dy[k]]:
                    break
                clear_memory.append(str(i+dx[k])+str(j+dy[k]))
                if k == 2:
                    clear = True
                    count += 1
            if clear:
                clear_result += clear_memory
                board[i][j] = ""
                for l in range(3):
                    board[i+dx[l]][j+dy[l]] = ""
    if count > 0:
        return True
    return False

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])