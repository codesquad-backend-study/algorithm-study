# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return

            if low < root.val:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)

            if low <= root.val <= high:
                self.sum += root.val

        dfs(root)
        return self.sum
