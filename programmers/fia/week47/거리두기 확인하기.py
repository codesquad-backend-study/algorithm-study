def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(places):
    answer = []

    for index in range(5):
        room = places[index]
        person = []

        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    person.append((i, j))

        def check(person1, person2):
            gap = distance(person1, person2)

            if gap > 2:
                return 1

            if gap == 1:
                return 0

            if gap == 2:
                row1 = person1[0]
                row2 = person2[0]
                col1 = person1[1]
                col2 = person2[1]

                if row1 == row2:
                    if room[row1][min(col1, col2) + 1] != 'X':
                        return 0
                elif col1 == col2:
                    if room[min(row1, row2) + 1][col1] != 'X':
                        return 0
                else:
                    if room[row1][col2] != 'X' or room[row2][col1] != 'X':
                        return 0

            return 1

        flag = False

        for i in range(len(person) - 1):
            if flag:
                break

            for j in range(i + 1, len(person)):
                if check(person[i], person[j]) == 0:
                    flag = True
                    break

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
