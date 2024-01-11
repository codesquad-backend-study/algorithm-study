from typing import List


# n: 외벽의 길이
# weak: 취약 지점의 위치를 담고 있는 배열
# disk: 각 친구가 1시간 동안 이동할 수 있는 거리를 담고 있는 배열
def solution(n: int, weak: List[int], dist: List[int]):
    answer = []
    clock = [i for i in range(0, n)]
    return min(answer)


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
