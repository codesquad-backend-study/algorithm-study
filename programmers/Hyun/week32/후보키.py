def solution(relation):
    col = len(relation[0])
    combi = []

    def combination(index, sub, limit):
        if len(sub) == limit:
            combi.append(tuple(sub))
            return

        if index >= col:
            return

        combination(index + 1, sub + [index], limit)
        combination(index + 1, sub, limit)

    for i in range(1, col + 1):
        combination(0, [], i)

    unique = []
    for each in combi:
        rows = set()
        for row in relation:
            tmp = []
            for key in each:
                tmp.append(row[key])
            rows.add(tuple(tmp))

        if len(rows) == len(relation):
            unique.append(each)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(set(unique[i])) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)
