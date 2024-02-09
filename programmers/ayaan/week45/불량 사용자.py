import itertools


def solution(user_id, banned_id):
    p = itertools.permutations(user_id, len(banned_id))
    result = []
    for case in p:
        match_cnt = 0
        for i in range(len(banned_id)):
            match = True
            if len(banned_id[i]) == len(case[i]):
                for j, val in enumerate(banned_id[i]):
                    if val == '*':
                        continue
                    elif val != case[i][j]:
                        match = False
                        break
                if match:
                    match_cnt += 1

        if match_cnt == len(banned_id):
            case = set(case)
            if case not in result:
                result.append(case)
    return len(result)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
