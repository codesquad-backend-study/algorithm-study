class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            root.left, root.right = root.right, root.left

        dfs(root)
        return root
