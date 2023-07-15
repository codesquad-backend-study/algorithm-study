# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        node_values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            for idx, _ in enumerate(node_values):
                node_values[idx] += node.val

            node_values.append(node.val)
            inorder(node.right)

        inorder(root)

        global order
        order = 0

        def change_val(node):
            if not node:
                return

            global order
            change_val(node.left)
            node.val = node_values[order]
            order += 1
            change_val(node.right)

        change_val(root)
        return root
