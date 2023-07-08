def solution(places):
    answer = []
    good = False

    for p in places:
        # (x, y) 좌표 설정 -> x가 상하로 움직이고 y가 좌우로 움직임
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for x in range(len(p)):
            for y in range(len(p)):
                # (|r1 - r2| + |c1 - c2| > 2)이어야 됨
                # "P"의 자리 사이가 "X"로 막혀있을 경우에만 허용

                if p[x][y] == 'P':
                    # P의 현재 좌표를 previous에 튜플로 저장
                    previous = (x, y)

        if good:  # 거리두기 지키면
            answer.append(1)
        else:  # 거리두기 안 지키면 (한 명이라도)
            answer.append(0)

    return answer


# answer: [1, 0, 1, 1, 1]
print(solution([["POOOP",
                 "OXXOX",
                 "OPXPX",
                 "OOXOX",
                 "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
