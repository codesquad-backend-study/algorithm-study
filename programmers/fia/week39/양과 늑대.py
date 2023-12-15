def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:  # 양이 늑대보다 많으면 결과를 저장해둔다
            answer.append(sheep)
        else:  # 그렇지 않다면 옳바르지 않은 접근이므로 돌아간다
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1  # 방문 표시하기
                if info[child] == 0:  # 만약 양이라면
                    dfs(sheep + 1, wolf)
                else:  # 만약 늑대라면
                    dfs(sheep, wolf + 1)
                visited[child] = 0  # 방문 표시 제거하기

    visited[0] = 1
    dfs(1, 0)

    return max(answer)


solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
