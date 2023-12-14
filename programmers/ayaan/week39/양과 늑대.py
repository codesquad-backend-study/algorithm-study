def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        # 모든 edge를 dfs로 탐색한다
        for p, c in edges:
            # children은 방문되지 않은 노드를 탐색한다
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                # dfs로 탐색하고 난 후에 다시 탐색하기 위해서 방문여부를 다시 0으로 만든다.
                visited[c] = 0

    dfs(1, 0)
    return max(answer)
