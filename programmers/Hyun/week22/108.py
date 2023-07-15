# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make(numbers):
            if not numbers:
                return None

            mid_idx = len(numbers) // 2
            node = TreeNode(numbers[mid_idx])

            node.left = make(numbers[:mid_idx])
            node.right = make(numbers[mid_idx + 1:])

            return node

        return make(nums)
