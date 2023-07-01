# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = []

        def find(root, prev, diameter):
            if not root:
                return 0

            if root.val != prev:
                find(root, root.val, 0)
                return 0

            left = find(root.left, root.val, diameter)
            right = find(root.right, root.val, diameter)

            diameter = max(left + right, diameter)
            ans.append(diameter)

            return max(left, right) + 1

        if not root:
            return 0
        find(root, root.val, 0)
        return max(ans)
