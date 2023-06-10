import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = []
        check_map = collections.defaultdict(int)

        lt, rt = 0, 1
        check_map[s[lt]] = 1
        tmp = s[lt]
        while lt < rt < len(s):
            if rt not in check_map:
                tmp += s[rt]
                check_map[s[rt]] = 1
                rt += 1
                continue

            answer.append(len(tmp))
            check_map = check_map.clear()
            lt = rt
            rt += 1
            tmp = s[lt]

        return max(answer)
