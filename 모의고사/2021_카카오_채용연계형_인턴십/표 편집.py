def solution(n, k, cmd):
    cells = [[i - 1, i + 1] for i in range(n)]
    cells[-1][1] = -1

    cursor = k
    stack = []
    for ins in cmd:
        if ins[0] == 'D':
            for _ in range(int(ins.split()[1])):
                cursor = cells[cursor][1]

        elif ins[0] == 'U':
            for _ in range(int(ins.split()[1])):
                cursor = cells[cursor][0]

        elif ins[0] == 'C':
            prev_pos = cells[cursor][0]
            next_pos = cells[cursor][1]
            if prev_pos != -1:
                cells[prev_pos][1] = next_pos
            if next_pos != -1:
                cells[next_pos][0] = prev_pos

            stack.append(cursor)

            if next_pos == -1:
                cursor = prev_pos
            else:
                cursor = next_pos


        elif ins[0] == 'Z':
            last_deleted_pos = stack.pop()
            prev_pos = cells[last_deleted_pos][0]
            next_pos = cells[last_deleted_pos][1]

            if prev_pos != -1:
                cells[prev_pos][1] = last_deleted_pos
            if next_pos != -1:
                cells[next_pos][0] = last_deleted_pos

    result = ["O"] * n
    for i in stack:
        result[i] = "X"

    return ''.join(result)
