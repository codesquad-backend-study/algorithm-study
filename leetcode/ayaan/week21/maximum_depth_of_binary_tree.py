# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return depth

            left = right = depth
            if node.left:
                left += 1
                left = max(left, dfs(node.left, left))
            if node.right:
                right += 1
                right = max(depth, dfs(node.right, right))
            return max(left, right)
        return dfs(root, 1)
