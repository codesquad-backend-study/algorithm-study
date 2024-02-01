import collections
import itertools


def solution(board, r, c):
    answer = float('inf')

    cdict = collections.defaultdict(list)
    for row in range(4):
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in itertools.permutations(cdict.keys(), len(cdict)):
        print(case)

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)
