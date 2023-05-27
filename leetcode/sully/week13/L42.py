from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        lt, rt = 0, 0
        start = 0
        # 처음 시작하는 부분 찾기 (y축은 벽으로 취급 안 해주잖아)
        for i in range(len(height)):
            if height[i] >= 1:
                start = i
                break

        # 메인 로직
        # while로 바꾸자
        for i in range(start, len(height)):
            # lt와 rt 구하는 로직
            lt = (i, height[i])
            for j in range(i, len(height)):
                if height[j] >= height[i]:
                    rt = (j, height[j])
                    break

            # lt와 rt의 index 값 사이에 있는 units of rain water 구하자
            # lt 블럭이든 rt 블럭이든 그 중 가장 작은 높이를 중심으로!
            # min_height: 더 낮은 높이를 기준으로 블럭을 계산해야 하니 미리 계산 후 저장
            min_height = min(lt[1], rt[1])
            # i + 1부터 j - 1까지 돌아주자 (물웅덩이만)
            # error: index error
            for k in range(lt[0] + 1, rt[0]):
                if height[k] < min_height:
                    answer += min_height - height[k]

            # j벽 그 다음부터 다시 돌아줘야 되니 위치 변경
            i = rt[0]

        return answer


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
