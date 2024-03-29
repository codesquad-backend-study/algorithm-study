# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            # 현재 노드가 low보다 작을 경우, 더 이상 왼쪽 가지는 탐색할 필요가 없음
            # 즉, 오른쪽만 탐색하도록 재귀 호출
            if node.val < low:
                return dfs(node.right)
            # 이것도 마찬가지
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
