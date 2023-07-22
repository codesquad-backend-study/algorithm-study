class Solution:
    # 반복해서 모든 리프 노드를 제거하면 남은 노드가 가장 짧은 트리의 루트가 된다.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 노드가 한개일 때 예외처리
        if n == 1:
            return [0]

        # 양방향 그래프로 초기화
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # 리프 노드 리스트 구하기
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 남은 노드가 1개 이하일 때까지 리프 노드를 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                # 제거한 리프 노드의 부모가 리프 노드가 되는지 확인
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        # 마지막으로 남은 리프 노드가 정답
        return leaves
