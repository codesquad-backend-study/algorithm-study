import itertools

def solution(orders, course):
    ans = []
    for cnt in course:
        menu_candidate = {}
        for order in orders:
            if len(order) < cnt:
                continue
            combinations = itertools.combinations(sorted(order), cnt)
            for combination in combinations:
                substr = ''.join(combination)
                if substr not in menu_candidate:
                    menu_candidate[substr] = 1
                else:
                    menu_candidate[substr] += 1

        menu_candidate = sorted(menu_candidate.items(), key=lambda x: x[1], reverse=True)
        next = 1
        if menu_candidate and menu_candidate[0][1] >= 2:
            ans.append(menu_candidate[0][0])

            while len(menu_candidate) > next and menu_candidate[0][1] == menu_candidate[next][1]:
                ans.append(menu_candidate[next][0])
                next += 1

    return sorted(ans)