from itertools import permutations


def solution(user_id, banned_id):
    groups = permutations(user_id, len(banned_id))

    def compare(group):
        for b_index, b_id in enumerate(banned_id):
            u_id = group[b_index]

            if len(u_id) != len(b_id):
                return False

            count = 0

            for char_index, char in enumerate(b_id):
                if char == '*' or u_id[char_index] == char:
                    count += 1

            if count != len(u_id):
                return False

        return True

    answer = set()

    for group in groups:
        if compare(group):
            answer.add(tuple(sorted(group)))

    return len(answer)
