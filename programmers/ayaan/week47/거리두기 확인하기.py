import collections


def search_distance(place):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_ok(x, y):
        visited = [[False] * 5 for _ in range(5)]
        visited[x][y] = True
        q = collections.deque([(x, y, 1)])

        while q:
            x, y, count = q.popleft()
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= 4 and 0 <= ny <= 4 and not visited[nx][ny] and count < 3:
                    if place[nx][ny] == 'O':
                        visited[nx][ny] = True
                        q.append((nx, ny, count + 1))
                    elif place[nx][ny] == 'P':
                        return False
        return True

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not is_ok(i, j):
                    return False
    return True


def solution(places):
    answer = []

    for place in places:
        if search_distance(place):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]])
