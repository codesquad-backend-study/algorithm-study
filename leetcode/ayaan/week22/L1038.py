# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root.right:
                dfs(root.right)

            self.sum += root.val
            root.val = self.sum

            if root.left:
                dfs(root.left)

        dfs(root)
        return root
