# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.fia.week21.number01 import TreeNode


class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum_values = []

        def inorder_traversal(node):
            if node is None:
                return

            inorder_traversal(node.right)
            if sum_values:
                node.val += sum_values[-1]
            sum_values.append(node.val)
            inorder_traversal(node.left)

        inorder_traversal(root)

        return root
