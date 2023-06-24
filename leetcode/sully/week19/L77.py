# from typing import List
#
#
# class Solution:
#     # [1, n] -> (1, n + 1) 범위
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         answer = []
#         # visited = [False] * k
#
#         def dfs(start: int, index: int, elements: List[int]):
#             if len(elements) == k:
#                 answer.append(elements[:])
#                 return
#
#             # visited[index] = True
#
#             for i in range(start, n + 1):
#                 # if not visited[i]:
#                 elements.append(i)
#                 dfs(start + 1, k + 1, elements)
#                 elements.pop()
#
#             # visited[index] = False
#
#         dfs(1, k, [])
#
#         return answer


from typing import List


class Solution:
    # [1, n] -> (1, n + 1) 범위
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start: int, index: int, elements: List[int]):
            if len(elements) == k:
                answer.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(i + 1, index + 1, elements)
                elements.pop()

        dfs(1, k, [])

        return answer
