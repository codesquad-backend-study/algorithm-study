# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.fia.week21.number01 import TreeNode


class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_of_values = [0]

        def preorder(node):
            if node is None:
                return

            if low <= node.val <= high:
                sum_of_values[0] += node.val

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return sum_of_values[0]
