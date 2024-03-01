def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    rowlist = ['O'] * n
    del_stack = []

    for command in cmd:
        command = command.split()
        if command[0] == 'D':
            for _ in range(int(command[1])):
                k = linked_list[k][1]
        elif command[0] == 'U':
            for _ in range(int(command[1])):
                k = linked_list[k][0]
        elif command[0] == 'C':
            prev = linked_list[k][0]
            next = linked_list[k][1]
            del_stack.append((k, prev, next))
            rowlist[k] = 'X'

            # k 위치 변경
            if next == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            # 행 삭제
            # 첫 번째 행인 경우
            if prev == -1:
                linked_list[next][0] = prev
            # 마지막 행인 경우
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        else:
            val, prev, next = del_stack.pop()
            rowlist[val] = 'O'

            if prev == -1:
                linked_list[next][0] = val
            elif next == n:
                linked_list[prev][1] = val
            else:
                linked_list[prev][1] = val
                linked_list[next][0] = val

    return ''.join(rowlist)


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
