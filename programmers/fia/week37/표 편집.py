def solution(n, k, cmd):
    linked_list = [[i - 1, i + 1, i] for i in range(n)]
    linked_list[0][0] = None
    linked_list[-1][1] = None

    removed = []
    current = linked_list[k]
    answer = ["O" for _ in range(n)]

    for c in cmd:
        if c.startswith("U"):
            for _ in range(int(c.split()[1])):
                current = linked_list[current[0]]
        elif c.startswith("D"):
            for _ in range(int(c.split()[1])):
                current = linked_list[current[1]]
        elif c == "C":
            prev_node = current[0]
            next_node = current[1]
            node_index = current[2]

            removed.append(current)

            answer[node_index] = 'X'

            if prev_node is None:
                linked_list[next_node][0] = None
            elif next_node is None:
                linked_list[prev_node][1] = None
            else:
                linked_list[prev_node][1] = next_node
                linked_list[next_node][0] = prev_node

            if next_node is None:
                current = linked_list[prev_node]
            else:
                current = linked_list[next_node]

        elif c == "Z":
            node = removed.pop()

            before = node[0]
            after = node[1]
            node_index = node[2]

            answer[node_index] = 'O'

            if before:
                linked_list[before][1] = node_index
            if after:
                linked_list[after][0] = node_index

    return ''.join(answer)
