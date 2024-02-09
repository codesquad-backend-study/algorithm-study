from itertools import permutations


def solution(user_id, banned_id):
    passed_group = set()

    for group in permutations(user_id, len(banned_id)):

        count = 0

        for index, user in enumerate(group):
            if len(user) == len(banned_id[index]):

                for char_index, char in enumerate(banned_id[index]):
                    if char != '*' and user[char_index] != char:
                        break
                else:
                    count += 1

        if count == len(banned_id):
            passed_group.add(tuple(sorted(list(group))))

    return len(passed_group)
