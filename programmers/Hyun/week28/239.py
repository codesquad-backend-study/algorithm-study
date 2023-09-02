class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()  # Store indices of elements in the current window

        for i in range(len(nums)):
            # Remove elements that are out of the current window from the front of the deque
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements that are smaller than the current element from the back of the deque
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # Add the current index to the back of the deque
            window.append(i)

            # Append the maximum element of the current window to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
