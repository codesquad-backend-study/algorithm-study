class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        water = 0

        left_idx = 0
        while height[left_idx] == 0:
            left_idx += 1

        while left_idx < len(height):
            right_idx = left_idx + 1

            while right_idx < len(height) and height[right_idx] <= height[left_idx]:
                right_idx += 1

            if right_idx == len(height):
                break

            sub_height = height[left_idx + 1:right_idx]
            water += (right_idx - left_idx - 1) * height[left_idx] - sum(sub_height)

            left_idx = right_idx

        right_idx = len(height) - 1
        while height[right_idx] == 0:
            right_idx -= 1

        while right_idx >= 0:
            left_idx = right_idx - 1

            while left_idx >= 0 and height[right_idx] > height[left_idx]:
                left_idx -= 1

            if left_idx < 0:
                break

            print(right_idx, left_idx)
            sub_height = height[left_idx + 1:right_idx]
            water += (right_idx - left_idx - 1) * height[right_idx] - sum(sub_height)

            right_idx = left_idx

        return water
