pick = [0, 0]

result = []


def go(n, start, pick):
    if n >= len(pick):
        result.append(pick[:])
        return

    for i in range(start, len(pick)):
        pick[i] += 1
        go(n + 1, i, pick)
        pick[i] -= 1


go(0, 0, pick)

print(result)

print(len(result))
