numbers = [1, 2, 3]
ans = []


def combi(index, sub, limit):
    if len(sub) >= limit:
        ans.append(sub)
        return

    if index >= len(numbers):
        return

    combi(index + 1, sub + [numbers[index]], limit)
    combi(index + 1, sub, limit)


combi(0, [], 1)
print(ans)
