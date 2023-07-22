# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            result = min(result, root.val - prev)

            prev = root.val
            root = root.right

        return result
