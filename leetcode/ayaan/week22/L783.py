# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -100001
    difference = 100001

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root.left:
                dfs(root.left)
            self.difference = min(self.difference, abs(self.prev - root.val))
            self.prev = root.val
            if root.right:
                dfs(root.right)

        dfs(root)
        return self.difference
