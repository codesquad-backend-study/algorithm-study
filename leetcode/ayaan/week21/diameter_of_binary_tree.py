class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_of_tree(root):
            if not root:
                return 0

            left_depth = depth_of_tree(root.left)
            right_depth = depth_of_tree(root.right)

            return max(left_depth, right_depth) + 1

        q = deque([root])
        diameter = 0
        while q:
            node = q.popleft()
            diameter = max(diameter, depth_of_tree(node.left) + depth_of_tree(node.right))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return diameter
