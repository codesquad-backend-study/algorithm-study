#  build_frame: [x, y, a, b]
#  x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
#  a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
#  b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.

def is_valid(installed: set):
    for x, y, a in installed:
        # 기둥은 바닥 위에 있거나,
        # 보의 한쪽 끝 부분 위에 있거나,
        # 다른 기둥 위에 있어야 함
        if a == 0:
            # y != 0: 기둥이 바닥에 있지 않고,
            # ((x, y, 1) not in installed and (x - 1, y, 1) not in installed): 양 옆에 보가 둘 다 없으면
            # (x, y - 1, 0) not in installed: 바로 아래에 기둥이 없고,
            # 틀린 조건이기 때문에 False 반환
            if (y != 0) and (
                    (x, y, 1) not in installed and (x - 1, y, 1) not in installed) and (
                    (x, y - 1, 0) not in installed):
                return False
        # 보는 한쪽 끝 부분이 기둥 위에 있거나,
        # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
        elif a == 1:
            # ((x, y - 1, 0) not in installed and (x + 1, y - 1, 0) not in installed): 바로 아래의 양 옆에 기둥이 둘 다 없고,
            # ((x - 1, y, 1) not in installed or (x + 1, y, 1) not in installed): 양 옆에 보가 하나라도 없으면
            # 틀린 조건이기 때문에 False 반환
            if ((x, y - 1, 0) not in installed and (x + 1, y - 1, 0) not in installed) and (
                    (x - 1, y, 1) not in installed or (x + 1, y, 1) not in installed):
                return False

    return True


def solution(n, build_frame):
    installed = set()

    for x, y, a, b in build_frame:
        # 삭제할 때
        if b == 0:
            installed.remove((x, y, a))

            # 규칙 위반 시, 다시 설치하여 삭제 취소
            if not is_valid(installed):
                installed.add((x, y, a))

        # 설치할 때
        elif b == 1:
            installed.add((x, y, a))

            # 규칙 위반 시, 다시 삭제하여 설치 취소
            if not is_valid(installed):
                installed.remove((x, y, a))

    return sorted(installed)


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
