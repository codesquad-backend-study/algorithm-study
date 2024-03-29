# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        dfs(root)

        return self.result
