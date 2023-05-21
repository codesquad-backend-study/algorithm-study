from typing import List


class Solution:
    # 최대 높이 막대는 왼쪽과 오른쪽을 가르는 장벽 역할을 함
    def trap(self, height: List[int]) -> int:
        answer = 0
        lt, rt = 0, len(height) - 1
        lt_max, rt_max = 0, 0

        # 가장 높이가 높은 막대인, "최대" 지점에서 좌우 포인터가 서로 만나게 됨
        # 딱 그 전까지 반복문 돌아주기
        while lt < rt:
            lt_max, rt_max = max(height[lt], lt_max), max(height[rt], rt_max)

            # 좌우 정해진 것 없이, 낮은 쪽에서 높은 쪽을 향해 포인터가 가운데로 점점 이동함
            # 오른쪽이 크면, 왼쪽이 이동
            if lt_max < rt_max:
                answer += lt_max - height[lt]
                lt += 1
            # 왼쪽이 크면, 오른쪽이 이동
            else:
                answer += rt_max - height[rt]
                rt -= 1

        return answer
