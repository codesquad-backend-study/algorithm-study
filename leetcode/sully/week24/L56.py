from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer: List[List[int]] = []

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            # 결과 리스트: answer, 현재 구간: inverval[0]
            # 결과 리스트가 비어 있거나
            # 현재 구간이 answer의 마지막 구간과 겹치지 않는다면
            # 현재 구간을 그대로 answer에 추가
            if not answer or interval[0] > answer[-1][1]:
                answer.append(interval)
                continue

            # continue에 안 걸렸으니 겹치는 구간이 있다는 뜻 -> 현재 구간과 answer의 마지막 구간을 병합하면 됨
            # answer의 마지막 구간의 끝 값 vs 현재 구간의 끝 값
            # 이것을 비교하여 더 큰 값이 끝에 오는 것이 맞으므로 그걸로 선택
            answer[-1][1] = max(answer[-1][1], interval[1])

        return answer
