# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def find(node, cnt):
            max_value = cnt

            if node.left:
                max_value = max(find(node.left, cnt + 1), max_value)

            if node.right:
                max_value = max(find(node.right, cnt + 1), max_value)

            return max_value

        current = root
        ans = 0
        queue = collections.deque([current])

        while queue:
            current = queue.popleft()

            left_dia = right_dia = 0
            if current.left:
                left_dia = find(current.left, 1)
                queue.append(current.left)
            if current.right:
                right_dia = find(current.right, 1)
                queue.append(current.right)

            ans = max(ans, left_dia + right_dia)

        return ans
