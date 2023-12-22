def solution(n, weak, dist):
    def permutation(arr, cnt):
        used = [False] * len(arr)
        groups = []

        def generate(picks):
            if len(picks) == cnt:
                groups.append(picks[:])
                return

            for i in range(len(arr)):
                if not used[i]:
                    picks.append(arr[i])
                    used[i] = True
                    generate(picks)
                    used[i] = False
                    picks.pop()

        generate([])
        return groups

    answer = n
    groups = permutation(dist, len(dist))
    flat = weak[:] + [i + n for i in weak]

    for idx in range(len(weak)):
        new_weak = flat[idx: idx + len(weak)]

        for group in groups:
            repair_man_idx, count = 0, 1
            possible_dist = new_weak[0] + group[repair_man_idx]
            for weak_point in new_weak:
                if weak_point > possible_dist:
                    count += 1
                    if count > len(dist):
                        break
                    repair_man_idx += 1
                    possible_dist = weak_point + group[repair_man_idx]

            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer
