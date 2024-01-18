def solution(commands):
    merged = [[(i, j) for j in range(51)] for i in range(51)]
    content = [['EMPTY'] * 51 for _ in range(51)]

    def update1(r, c, value):
        x, y = merged[r][c]
        content[x][y] = value

    def update2(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if content[i][j] == value1:
                    content[i][j] = value2

    def merge(r1, c1, r2, c2):
        x1, y1 = merged[r1][c1]
        x2, y2 = merged[r2][c2]

        for i in range(1, 51):
            for j in range(1, 51):
                if merged[i][j] == (x2, y2):
                    merged[i][j] = (x1, y1)

        if content[x1][y1] == 'EMPTY':
            if content[x2][y2] != 'EMPTY':
                content[x1][y1] = content[x2][y2]

    def unmerge(r, c):
        x, y = merged[r][c]
        tmp = content[x][y]

        for i in range(1, 51):
            for j in range(1, 51):
                if merged[i][j] == (x, y):
                    merged[i][j] = (i, j)
                    content[i][j] = 'EMPTY'

        content[r][c] = tmp

    def print_value(r, c):
        x, y = merged[r][c]
        answer.append(content[x][y])

    answer = []

    for command in commands:
        command = command.split()
        c = command[0]

        if c == 'UPDATE':
            if len(command) == 3:
                update2(command[1], command[2])
            else:
                update1(int(command[1]), int(command[2]), command[3])
        elif c == 'MERGE':
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif c == 'UNMERGE':
            unmerge(int(command[1]), int(command[2]))
        elif c == 'PRINT':
            print_value(int(command[1]), int(command[2]))

    return answer


print(solution(
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1",
     "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
