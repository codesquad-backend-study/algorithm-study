def solution(n, k, cmd):
    deleted = set()
    stack = []
    db = []

    for i in range(n):
        if i == 0:
            db.append([None, 1])
        elif i == n - 1:
            db.append([i - 1, None])
        else:
            db.append([i - 1, i + 1])

    cursor = k
    for ins in cmd:
        splited = ins.split()

        if splited[0] == 'U':
            for _ in range(int(splited[1])):
                cursor = db[cursor][0]
        elif splited[0] == 'D':
            for _ in range(int(splited[1])):
                cursor = db[cursor][1]
        elif splited[0] == 'C':
            stack.append(cursor)
            deleted.add(cursor)
            prev_node = db[cursor][0]
            next_node = db[cursor][1]

            if prev_node is None:
                db[next_node][0] = None
                cursor = next_node
            elif next_node is None:
                db[prev_node][1] = None
                cursor = prev_node
            else:
                db[prev_node][1] = next_node
                db[next_node][0] = prev_node
                cursor = next_node

        elif splited[0] == 'Z':
            last_deleted = stack.pop()
            deleted.remove(last_deleted)
            prev_node = db[last_deleted][0]
            next_node = db[last_deleted][1]

            if prev_node is None:
                db[next_node][0] = last_deleted
            elif next_node is None:
                db[prev_node][1] = last_deleted
            else:
                db[prev_node][1] = last_deleted
                db[next_node][0] = last_deleted

    ans = ""
    for i in range(n):
        if i in deleted:
            ans += 'X'
        else:
            ans += 'O'

    return ans
