# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 개수 N
# 사용자가 현재 진행중인 스테이지 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 담아서 return
## 실패율이 같은 스테이지가 있다면, 작은 번호 스테이지 먼저
# 스테이지에 도달한 유저가 없는 경우, 해당 스테이지 실패율은 0
import collections


def solution(N, stages):
    stages.sort()
    rate = {i: 0 for i in range(1, N + 1)}

    counter = collections.Counter(stages)
    key_set = sorted(counter.keys())

    total = len(stages)
    for key in key_set:
        if key == N + 1:
            break
        rate[key] = counter[key] / total
        total -= counter[key]

    ans = []
    for idx, _ in sorted(rate.items(), key=lambda x: (-x[1], x[0])):
        ans.append(idx)
    return ans
