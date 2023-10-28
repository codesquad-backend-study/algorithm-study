import itertools


def solution(user_id, banned_id):
    combies = list(itertools.permutations(user_id, len(banned_id)))

    def word_compare(ban, user):
        if len(ban) == len(user):
            for i in range(len(ban)):
                if ban[i] != user[i] and ban[i] != '*':
                    return False
            return True
        return False

    ans = set()

    for combi in combies:
        banned_tmp = banned_id[:]
        for user in combi:
            for idx, ban in enumerate(banned_tmp):
                if word_compare(ban, user):
                    del banned_tmp[idx]
                    break

        if not banned_tmp:
            ans.add(tuple(sorted(list(combi))))

    return len(ans)
