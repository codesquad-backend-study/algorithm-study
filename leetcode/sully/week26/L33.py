from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            # (rt - lt) // 2: 탐색 범위의 중간 인덱스
            # 거기에 lt를 더하면 -> 실제 중간 인덱스가 됨
            mid = (rt - lt) // 2 + lt

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정렬되었으면
            if nums[lt] <= nums[mid]:
                # 왼쪽 절반에서 target을 찾아야 하는지 확인
                if nums[mid] > target >= nums[lt]:
                    # nums[mid]가 target보다 크니 당연히 빼줘야 됨
                    mid -= rt
                    rt -= 1
                    continue

                mid += lt
                lt += 1
                continue

            # 오른쪽 절반이 정렬되었으면
            # 오른쪽 절반에서 target을 찾아야 하는지 확인
            if nums[mid] < target <= nums[rt]:
                # nums[mid]가 target보다 작으니 당연히 더해줘야 됨
                mid += lt
                lt += 1
                continue

            mid -= rt
            rt -= 1

        return -1
