import sys


def solution(n, m, x, y, r, c, k):
    sys.setrecursionlimit(3000)

    # n : 미로의 세로 길이 - x - r
    # m : 미로의 가로 길이 - y - c
    # 사전순: d(하) - l(좌) - r(우) - u(상)

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    char = ['d', 'l', 'r', 'u']

    global answer
    answer = 'impossible'

    def manhattan_distance(cx, cy):
        return abs(r - cx) + abs(c - cy)

    def dfs(cx, cy, remain, route):
        global answer

        # 남은 거리보다 갈 수 있는 거리가 짧다면 안된다
        if remain < manhattan_distance(cx, cy):
            return

        # 짝수가 아니라면 도착할 수 없다
        if (remain - manhattan_distance(cx, cy)) % 2 == 1:
            return

        if remain == 0:
            if cx == r and cy == c:
                answer = ''.join(route)
                return

        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy

            if 0 < nx <= n and 0 < ny <= m:
                route.append(char[i])
                dfs(nx, ny, remain - 1, route)

                if answer != 'impossible':
                    return

                route.pop()

    dfs(x, y, k, [])

    return answer
