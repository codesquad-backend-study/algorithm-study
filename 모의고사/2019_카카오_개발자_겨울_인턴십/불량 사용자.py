import itertools


def match_check(users, banned_id):  # 유저리스트와 제재목록 비교
    for i in range(len(users)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] != users[i][j]:
                return False
    return True


def user_list_check(user_list, banned_id):  # 유저리스트를 순열로 모든 경우의 수 구함
    for users in itertools.permutations(user_list, len(user_list)):
        if match_check(users, banned_id):
            return True
    return False


def solution(user_id, banned_id):
    a = list(itertools.combinations(user_id, len(banned_id)))
    cnt = 0
    for user_list in a:  # 유저리스트를 조합으로 중복없이 구함
        if user_list_check(user_list, banned_id):
            cnt += 1

    return cnt



