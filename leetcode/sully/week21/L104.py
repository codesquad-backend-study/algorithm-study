import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        dq = collections.deque([root])
        depth = 0

        while dq:
            depth += 1

            for _ in range(len(dq)):
                cur_root = dq.popleft()

                if cur_root.left:
                    dq.append(cur_root.left)

                if cur_root.right:
                    dq.append(cur_root.right)

        return depth
