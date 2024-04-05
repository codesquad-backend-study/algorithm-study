# 유일성 최소성

# 8개 중 -> 2^8
# 20개에 대해 반복
# 256 * 20

# 0,1 - 1,2 - 2,3구분, # 0 1 ->x 0 1 2
import itertools


def contains(a, b):
    for i in a:
        if i not in b:
            return False
    return True


def calculate(picks, relation, ans):
    if not picks:
        return False

    for a in ans:
        if contains(a, picks):
            return False

    unique = set()
    for each in relation:
        tmp = []
        for i in picks:
            tmp.append(each[i])
        unique.add(tuple(tmp))

    return len(unique) == len(relation)


def solution(relation):
    ans = set()
    idx = [i for i in range(len(relation[0]))]
    for i in range(len(idx) + 1):
        for picks in itertools.combinations(idx, i):
            if calculate(picks, relation, ans):
                ans.add(tuple(picks))

    print(ans)
    return len(ans)
