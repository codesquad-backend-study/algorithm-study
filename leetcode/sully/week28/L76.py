import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        t_length = len(t)
        lt, start, end = 0, 0, 0

        for rt, c in enumerate(s, 1):
            if counter[c] > 0:
                t_length -= 1
            counter[c] -= 1

            if t_length == 0:
                while lt < rt and counter[s[lt]] < 0:
                    counter[s[lt]] += 1
                    lt += 1

                if not end or rt - lt <= end - start:
                    start, end = lt, rt
                    counter[s[lt]] += 1
                    t_length += 1
                    lt += 1

        return s[start:end]
