import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = []
        check_map = collections.defaultdict(int)

        lt, rt = 0, 1
        check_map[s[lt]] = 1
        tmp = s[lt]
        while lt < rt < len(s):
            if s[rt] not in check_map:
                check_map[s[rt]] = 1
                tmp += s[rt]
                rt += 1
                continue

            answer.append(tmp)
            check_map.clear()
            lt += 1
            rt = lt + 1
            check_map[s[lt]] = 1
            tmp = s[lt]

        answer.sort(key=len)
        print(answer)
        return len(answer[-1])
