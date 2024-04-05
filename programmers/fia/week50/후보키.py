from itertools import combinations


def solution(relation):
    col_num = len(relation[0])
    row_num = len(relation)

    if col_num == 1:
        return col_num

    if row_num == 1:
        return col_num

    groups = []
    for i in range(1, col_num + 1):
        groups.extend(combinations(range(col_num), i))

    possible = []

    for group in groups:
        data = set()

        for r in range(row_num):
            row = []
            for c in group:
                row.append(relation[r][c])

            data.add(tuple(row))

        if len(data) == row_num:
            possible.append(group)

    answer = set(possible)
    for i in range(len(possible)):
        for j in range(i + 1, len(possible)):
            if len(possible[i]) == len(set(possible[i]) & set(possible[j])):
                answer.discard(possible[j])

    return len(answer)
