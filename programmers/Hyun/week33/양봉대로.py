# 어피치 먼저 쏜다.
# 더 많은 화살을 k 점에 맞힌 선수가 딱 k 점 획득 , 같으면 어피치가 획득
# 최종 점수가 많으면 우승, 같으면 어피치가 우승
# 어피치가 n 발을 쏜 상황, 이제 라이언 차례
# 라이언이 우승하려면 어떻게 맞추어야 할까?

# n = 화살개수, info = 맞춘 과녁 점수 배열 [10점 개수, 9점 개수, ...]
# solution = 어떻게 과녁을 맞춰야 할까? [10점 개수, 9점 개수... ] 순으로 반환
# 라이언이 무조건 지는 경우 [-1] 반환
# 라이언이 우승할 수 있는 경우의 수가 여러개라면 가장 낮은 점수를 많이 맞힌 경우를 return
import collections


def solution(n, info):
    result = collections.defaultdict(list)

    global max_diff
    max_diff = -1

    picks = [0] * 11

    def find_lowest_hit(hits):
        ans = hits[0]

        for each in hits:
            for i in range(10, -1, -1):
                if each[i] > ans[i]:
                    ans = each
                    break
                elif each[i] < ans[i]:
                    break
        return ans

    def calculate(picks):
        lion = appeach = 0
        for i in range(10):
            if info[i] < picks[i]:
                lion += 10 - i
            elif info[i] != 0 and info[i] >= picks[i]:
                appeach += 10 - i

        return lion > appeach, lion - appeach

    def go(cnt, start, picks):
        global max_diff
        if cnt >= n:
            lion_win, score_diff = calculate(picks)
            if lion_win:
                max_diff = max(max_diff, score_diff)
                result[score_diff].append(picks[:])
            return

        for i in range(start, 11):
            picks[i] += 1
            go(cnt + 1, i, picks)
            picks[i] -= 1

    go(0, 0, picks)

    if not result:
        return [-1]

    return find_lowest_hit(result[max_diff])
