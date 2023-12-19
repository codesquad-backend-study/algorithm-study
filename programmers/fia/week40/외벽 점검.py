def solution(n, weak, dist):
    # 2배로 늘려서 직선으로 만들기
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    # 친구들의 모든 순열 찾기
    def permutation():
        results = []
        visited = [False] * len(dist)

        def generate(temp):
            if len(temp) == len(dist):
                results.append(temp[:])

            for i in range(len(dist)):
                if not visited[i]:
                    temp.append(dist[i])
                    visited[i] = True
                    generate(temp)
                    temp.pop()
                    visited[i] = False

        generate([])

        return results

    groups = permutation()
    answer = len(dist) + 1

    for start in range(len(weak) // 2):
        for group in groups:
            friend = 1

            # 현재 친구가 점검 가능한 취약점 구하기
            # position = 현재 취약점 숫자 (ex 1) + 현재 친구의 이동 가능 거리 (ex 1) = 2
            position = weak[start] + group[friend - 1]

            # 시작점부터 모든 취약점 확인
            for i in range(start, start + len(weak) // 2):
                if position < weak[i]:
                    friend += 1

                    if friend > len(dist):
                        break

                    position = weak[i] + group[friend - 1]

            answer = min(friend, answer)

    return answer if answer <= len(dist) else -1
