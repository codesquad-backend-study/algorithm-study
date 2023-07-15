# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        if not root1 and root2:
            return None

        root = TreeNode(root1.val + root2.val)
        queue = collections.deque([(root, root1, root2)])

        while queue:
            node, node1, node2 = queue.popleft()

            if (node1 and node1.left) or (node2 and node2.left):
                val = 0
                left_elements = collections.deque()

                if node1 and node1.left:
                    val += node1.left.val
                    left_elements.append(node1.left)
                else:
                    left_elements.append(None)
                if node2 and node2.left:
                    val += node2.left.val
                    left_elements.append(node2.left)
                else:
                    left_elements.append(None)

                node.left = TreeNode(val)
                left_elements.appendleft(node.left)
                queue.append(tuple(left_elements))

            if (node1 and node1.right) or (node2 and node2.right):
                val = 0
                right_elements = collections.deque()

                if node1 and node1.right:
                    val += node1.right.val
                    right_elements.append(node1.right)
                else:
                    right_elements.append(None)
                if node2 and node2.right:
                    val += node2.right.val
                    right_elements.append(node2.right)
                else:
                    right_elements.append(None)

                node.right = TreeNode(val)
                right_elements.appendleft(node.right)
                queue.append(tuple(right_elements))

        return root
