# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        sub_cnt = {i: idx for idx, i in enumerate(inorder)}

        def find(inorder_start, inorder_end, preorder_start, preorder_end):
            if preorder_end == preorder_start:
                return None
            root_idx = preorder[preorder_start]
            root = TreeNode(root_idx)

            if preorder_end - preorder_start <= 1:
                return root

            left_cnt = sub_cnt[root_idx] - inorder_start
            right_cnt = inorder_end - sub_cnt[root_idx] - 1

            root.left = find(inorder_start, inorder_start + left_cnt, preorder_start + 1, preorder_start + 1 + left_cnt)

            root.right = find(inorder_end - right_cnt, inorder_end, preorder_end - right_cnt, preorder_end)

            return root

        return find(0, len(inorder), 0, len(preorder))





