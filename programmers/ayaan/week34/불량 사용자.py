import itertools
import re

def solution(user_id, banned_id):
    answer = set()
    user_permutation = list(itertools.permutations(user_id, len(banned_id)))
    for user in user_permutation:
        is_match = False
        for i, id in enumerate(user):
            p = re.compile(banned_id[i].replace('*', '\w') + '$')
            if p.match(id) is None:
                is_match = False
                break
            else:
                is_match = True
        if is_match:
            answer.add(tuple(sorted(list(user))))
    return len(answer)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
