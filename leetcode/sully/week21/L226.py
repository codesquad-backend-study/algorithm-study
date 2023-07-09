# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = collections.deque([root])

        while dq:
            # pop(): 바텀업
            # popleft(): 탑다운
            node = dq.popleft()

            if node:
                node.left, node.right = node.right, node.left

                dq.append(node.left)
                dq.append(node.right)

        return root
