# 후보키
from itertools import combinations


def solution(relation):
    column_count = len(relation[0])
    row_count = len(relation)

    if column_count == 1:
        return column_count

    if row_count == 1:
        return column_count

    # 모든 경우의 수
    groups = []

    for i in range(1, column_count + 1):
        groups.extend(combinations(range(column_count), i))

    # 유일성
    unique = []

    for group in groups:
        data = [tuple(row[index] for index in group) for row in relation]

        if len(set(data)) == row_count:
            unique.append(group)

    # 최소성
    answer = set(unique)

    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)
