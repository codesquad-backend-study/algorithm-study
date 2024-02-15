import collections


def bfs(destination, left_num, right_num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dist = [[-1] * 3 for _ in range(4)]
    destination -= 1

    queue = collections.deque()
    dist[destination // 3][destination % 3] = 0
    queue.append((destination % 3, destination // 3))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 3 and 0 <= ny < 4:
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))

    left_num -= 1
    right_num -= 1
    return dist[left_num // 3][left_num % 3], dist[right_num // 3][right_num % 3]


def solution(numbers, hand):
    ans = []
    left = 10
    right = 12
    for num in numbers:
        if num in [1, 4, 7]:
            ans.append('L')
            left = num
        elif num in [3, 6, 9]:
            ans.append('R')
            right = num
        else:
            if num == 0:
                num = 11
            left_dist, right_dist = bfs(num, left, right)
            if left_dist > right_dist:
                ans.append('R')
                right = num
            elif left_dist < right_dist:
                ans.append('L')
                left = num
            else:
                if hand == 'right':
                    ans.append('R')
                    right = num
                else:
                    ans.append('L')
                    left = num

    return ''.join(ans)
