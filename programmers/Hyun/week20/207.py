class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visit = [False] * (numCourses + 1)

        graph = [[] for _ in range(numCourses)]

        for x, y in prerequisites:
            if x == y:
                return False
            graph[x].append(y)

        global circle
        circle = False

        def dfs(node, prev_nodes):
            global circle
            if circle:
                return

            visit[node] = True

            for i in graph[node]:
                if i in prev_nodes:
                    circle = True
                    return

                if not visit[i] and not circle:
                    dfs(i, prev_nodes + [node])

        for i in range(numCourses):
            if not visit[i]:
                dfs(i, [])
        return not circle
