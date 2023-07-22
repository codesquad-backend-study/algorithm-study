class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        result = root = TreeNode(nums[mid])

        def bst(root, num_list, mid):
            left_list = num_list[:mid]
            right_list = num_list[mid + 1:]

            if len(left_list) > 0:
                root.left = TreeNode(left_list[len(left_list) // 2])
                bst(root.left, left_list, len(left_list) // 2)

            if len(right_list) > 0:
                root.right = TreeNode(right_list[len(right_list) // 2])
                bst(root.right, right_list, len(right_list) // 2)

        bst(root, nums, mid)
        return result
