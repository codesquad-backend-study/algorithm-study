from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        # 테케 35/48 시간초과 코드
        len_tem = len(temperatures)
        for i in range(len_tem - 1):
            found = False
            cnt = 0
            for j in range(i + 1, len_tem):
                cnt += 1
                if temperatures[i] < temperatures[j]:
                    found = True
                    break

            if found:
                answer.append(cnt)
            else:
                answer.append(0)

        # 8번째 줄에서 i가 마지막일 때는 할 필요가 없어서 안 해줬으니 해주자
        # 마지막은 무조건 0이 될 수밖에 없음
        answer.append(0)

        return answer
