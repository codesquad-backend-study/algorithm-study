import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0

        lt, rt = 0, 0
        counter = collections.Counter()

        while rt < len(s):
            counter[s[rt]] += 1
            # lt부터 rt까지 가장 많은 문자의 개수
            most_common = counter.most_common(1)[0][1]
            # 바꿔야 할 문자 수
            remain = rt - lt + 1 - most_common

            # 바꿔야 할 문자 수가 바꿀 수 있는 문자 수보다 많을 때
            if remain > k:
                counter[s[lt]] -= 1
                # lt를 증가시켜 윈도우 수를 줄임
                lt += 1

            answer = max(rt - lt + 1, answer)
            rt += 1

        return answer
