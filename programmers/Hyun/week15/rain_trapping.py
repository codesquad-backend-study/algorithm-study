class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        water = 0

        left = 0
        while height[left] <= 0:
            left += 1

        while left < len(height):
            right = left + 1
            while right < len(height) and height[left] > height[right]:
                right += 1

            if right >= len(height):
                break

            water += height[left] * (right - left - 1) - sum(height[left + 1:right])

            left = right

        right = len(height) - 1
        while height[right] <= 0:
            right -= 1

        while right >= 0:
            left = right - 1
            while left >= 0 and height[left] <= height[right]:
                left -= 1

            if left < 0:
                break

            water += height[right] * (right - left - 1) - sum(height[left + 1:right])

            right = left

        return water







