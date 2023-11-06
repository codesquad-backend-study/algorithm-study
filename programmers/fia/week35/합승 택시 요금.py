import heapq


def solution(n, s, a, b, fares):
    UNVISITED = 100_000 * 200 * 2

    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    # 시작 지점부터 각 노드까지 비용 계산
    def base():
        costs = [UNVISITED] * (n + 1)
        costs[s] = 0
        queue = []
        heapq.heappush(queue, (0, s))

        while queue:
            cost, node = heapq.heappop(queue)

            if costs[node] < cost:
                continue

            for no, co in graph[node]:
                if costs[no] > costs[node] + co:
                    costs[no] = costs[node] + co
                    heapq.heappush(queue, (costs[node] + co, no))

        return costs

    # 중간 지점에서 A, B까지의 각각의 비용 계산
    def find(start):
        costs = [UNVISITED] * (n + 1)
        costs[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            cost, node = heapq.heappop(queue)

            if costs[node] < cost:
                continue

            for no, co in graph[node]:
                if costs[no] > costs[node] + co:
                    costs[no] = costs[node] + co
                    heapq.heappush(queue, (costs[node] + co, no))

        return costs[a] + costs[b]

    answer = UNVISITED
    bases = base()

    for mid in range(1, n + 1):
        answer = min(answer, find(mid) + bases[mid])

    return answer

# 효율성  테스트
# 테스트 1 〉	통과 (20.79ms, 10.2MB)
# 테스트 2 〉	통과 (114.14ms, 10.6MB)
# 테스트 3 〉	통과 (39.66ms, 10.3MB)
# 테스트 4 〉	통과 (39.01ms, 10.2MB)
# 테스트 5 〉	통과 (39.03ms, 10.2MB)
# 테스트 6 〉	통과 (40.17ms, 10.4MB)
# 테스트 7 〉	통과 (1149.63ms, 15.6MB)
# 테스트 8 〉	통과 (1017.49ms, 15.6MB)
# 테스트 9 〉	통과 (1020.99ms, 15.6MB)
# 테스트 10 〉	통과 (1012.30ms, 15.4MB)
# 테스트 11 〉	통과 (902.58ms, 15.6MB)
# 테스트 12 〉	통과 (544.24ms, 12.9MB)
# 테스트 13 〉	통과 (560.11ms, 12.8MB)
# 테스트 14 〉	통과 (568.14ms, 12.9MB)
# 테스트 15 〉	통과 (546.37ms, 12.9MB)
# 테스트 16 〉	통과 (33.78ms, 10.2MB)
# 테스트 17 〉	통과 (37.63ms, 10.4MB)
# 테스트 18 〉	통과 (33.35ms, 10.4MB)
# 테스트 19 〉	통과 (87.44ms, 10.5MB)
# 테스트 20 〉	통과 (141.43ms, 10.6MB)
# 테스트 21 〉	통과 (138.06ms, 10.6MB)
# 테스트 22 〉	통과 (610.21ms, 12.9MB)
# 테스트 23 〉	통과 (536.99ms, 12.9MB)
# 테스트 24 〉	통과 (566.91ms, 12.9MB)
# 테스트 25 〉	통과 (22.83ms, 10.3MB)
# 테스트 26 〉	통과 (19.07ms, 10.3MB)
# 테스트 27 〉	통과 (124.31ms, 10.5MB)
# 테스트 28 〉	통과 (146.09ms, 10.6MB)
# 테스트 29 〉	통과 (12.72ms, 10.2MB)
# 테스트 30 〉	통과 (14.17ms, 10.3MB)
