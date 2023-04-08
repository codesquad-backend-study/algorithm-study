# m: 폭, n: 높이, board(list): 배치 정보
def solution(m, n, board):
    answer = 0

    # 4개 블록 찾기 -> 추출해줬다가 remove_set 떔에 걍 안 해줌
    for i in range(m - 1):
        for j in range(n - 1):
            # 일단 현재 위치가 0이 아니어야 이 로직이 작동되도록 해야 함
            if board[i][j] != 0:
                # 인접하는 4칸이 같으면
                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i + 1][j] == \
                        board[i + 1][j + 1] and board[i][j + 1] == board[i + 1][j + 1]:
                    answer += 1

                    # 아래처럼 하면 board를 2차원 배열로 만들어야 함
                    # 그럼 그냥 remove한 원소들을 따로 저장하자
                    # --------------------------------------------------------
                    # # 그리고 여기서 그 배열들을 remove 해줘야지 (값으로 삭제하는 함수)
                    # board.remove(board[i][j])
                    # board.remove(board[i][j + 1])
                    # board.remove(board[i + 1][j])
                    # board.remove(board[i][j + 1])

                    remove_list = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]

    # remove_list에 있는 원소들은 건너뛰면 되려나?
    # 아래로 쭉 내리는 정렬은 어떤 식으로 하면 될까
    # 아 아무리 생각해도 초반에 2차원 배열로 변환했어야 될 거 같은데
    for i in range(m - 1):
        for j in range(n - 1):


    return answer


# answer: 14
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# answer: 15
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
