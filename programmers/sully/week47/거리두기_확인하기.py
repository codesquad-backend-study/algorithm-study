import queue
from typing import List

# 상, 하, 좌, 우
d = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(places: List[List[str]]) -> List[int]:
    answer: List[int] = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def check(place: List[str]) -> bool:
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P' and not bfs(place, r, c):
                return False

    return True


def bfs(place: List[str], row: int, col: int) -> bool:
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = queue.Queue()
    visited[row][col] = True
    # 행, 열, 거리
    q.put((row, col, 0))

    while not q.empty():
        current_q = q.get()

        # 최대 2칸 거리까지만 확인하면 되니
        if current_q[2] > 2:
            continue

        # 2칸 이내 거리에 다른 사람이 있어 안전하지 않다는 의미
        if (current_q[2] != 0) and (place[current_q[0]][current_q[1]] == 'P'):
            return False

        # 상하좌우 네 방향 탐색
        for i in range(4):
            new_row = current_q[0] + d[i][0]
            new_col = current_q[1] + d[i][1]

            # 맵 범위를 벗어나거나
            # 이미 방문한 노드이거나
            # 벽(X)이면 다음 위치를 무시하고 다음 반복문으로
            if (new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4) or (
                    visited[new_row][new_col]) or (
                    place[new_row][new_col] == 'X'):
                continue

            # 다음 위치가 방문하지 않은 비어 있는 공간이라면 visited 갱신 후
            # 다음 위치와 이동 거리(현재 거리 + 1)를 큐에 추가
            visited[new_row][new_col] = True
            q.put((new_row, new_col, current_q[2] + 1))

    return True
