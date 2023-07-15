import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root, 1)])
        depth = 0

        while queue:
            node, count = queue.popleft()
            depth = max(depth, count)
            if node.left:
                queue.append((node.left, count + 1))
            if node.right:
                queue.append((node.right, count + 1))
        return depth
