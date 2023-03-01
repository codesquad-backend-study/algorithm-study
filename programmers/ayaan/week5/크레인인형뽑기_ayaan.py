def solution(board, moves):
    answer = 0
    
    stack = []
    
    for i in moves:
        for j, line in enumerate(board):
            val = line[i-1]
            if val == 0:
                continue
            
            if len(stack) != 0 and stack[-1] == val:
                stack.pop()
                answer += 2
            else :
                stack.append(val)
            
            board[j][i-1] = 0
            break
    
    return answer

# 1 5 3 5 1 2 1 4
result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(result)

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]
