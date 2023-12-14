from typing import List


def solution(info: List[int], edges: List[List[int]]) -> int:
    ROOT_INDEX = 0
    SHEEP_NUMBER = 0
    WOLF_NUMBER = 1
    NOT_VISITED_NUMBER = 0
    VISITED_NUMBER = 1

    answer = []
    visited = [NOT_VISITED_NUMBER] * len(info)

    def dfs(sheep, wolf):
        if sheep <= wolf:
            return

        answer.append(sheep)

        # edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태
        for parent_node, child_node in edges:
            # 부모 노드가 방문된 상태, 자식 노드가 방문되지 않은 상태 -> 이래야 중복 방문을 피할 수 있음
            if visited[parent_node] and not visited[child_node]:
                visited[child_node] = VISITED_NUMBER

                if info[child_node] == SHEEP_NUMBER:
                    dfs(sheep + 1, wolf)
                elif info[child_node] == WOLF_NUMBER:
                    dfs(sheep, wolf + 1)

                visited[child_node] = NOT_VISITED_NUMBER

    visited[ROOT_INDEX] = VISITED_NUMBER

    # 0번 노드(루트 노드)에는 항상 양이 있음 (늑대는 없음)
    dfs(1, 0)

    return max(answer)
