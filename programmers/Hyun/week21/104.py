# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = []

        if not root:
            return 0

        queue = collections.deque([(root, 1)])

        while queue:
            node, cnt = queue.popleft()
            counter.append(cnt)

            if node.left:
                queue.append((node.left, cnt + 1))

            if node.right:
                queue.append((node.right, cnt + 1))

        return max(counter)
