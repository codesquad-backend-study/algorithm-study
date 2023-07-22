# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_val = preorder[0]
        root = TreeNode(root_val)

        def build(root, start_pre, end_pre, start_in, end_in):
            if start_pre > end_pre or start_in > end_in:
                return
            mid = inorder.index(root.val)
            left_cnt = mid - start_in
            right_cnt = end_in - mid

            root.left = TreeNode(preorder[start_pre + 1])
            root.right = TreeNode(preorder[end_in - right_cnt])

            build(root.left, start_pre + 1, start_pre + left_cnt, start_in, start_in + left_cnt - 1)
            build(root.right, end_pre - right_cnt, end_pre, end_pre - right_cnt + 1, end_pre)

        build(root, 0, len(preorder) - 1, 0, len(inorder) - 1)
        return root
