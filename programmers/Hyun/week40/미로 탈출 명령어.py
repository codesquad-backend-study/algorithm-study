# n, m => 격자 크기, n 세로길이, m 가로길이
# x, y => 출발 지점 1,1 부터 시작
# r, c => 탈출 지점  r = y좌표, c = x좌표
# k 번 이동해서 탈출 경로를 사전순으로

import collections, sys

sys.setrecursionlimit(5000)


def solution(n, m, x, y, r, c, k):
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]
    move_ins = ['d', 'l', 'r', 'u']

    global find, ans
    find = False
    ans = 'impossible'
    buf = []

    def calculate_end_distance_from(cx, cy):
        return abs(c - cx) + abs(r - cy)

    def go(remain, cx, cy):
        global find, ans

        if find:
            return

        if remain < calculate_end_distance_from(cx, cy):
            return

        if (remain - calculate_end_distance_from(cx, cy)) % 2 == 1:
            return

        if remain == 0:
            if cx == c and cy == r:
                ans = ''.join(buf)
                find = True
            return

        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 < nx <= m and 0 < ny <= n:
                buf.append(move_ins[i])
                go(remain - 1, nx, ny)
                buf.pop()

    go(k, y, x)
    return ans
