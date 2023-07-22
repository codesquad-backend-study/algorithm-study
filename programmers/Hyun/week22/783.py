# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -10 ** 5
    diff = 10 ** 5

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.diff = min(self.diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.diff
