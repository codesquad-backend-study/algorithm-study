import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    is_balanced = None

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def traversal(node, depth):
            if node is None:
                return depth - 1

            left_depth = traversal(node.left, depth + 1)
            right_depth = traversal(node.right, depth + 1)

            if -1 > left_depth - right_depth or 1 < left_depth - right_depth:
                self.is_balanced = False

            return max(left_depth, right_depth)

        traversal(root, 0)

        return self.is_balanced
