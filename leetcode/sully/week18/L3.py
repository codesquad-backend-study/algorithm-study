import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_map = collections.defaultdict(int)
        start = max_len = 0

        INDEX_PLUS = 1
        for i, c in enumerate(s):
            if c in used_map and start <= used_map[c]:
                start = used_map[c] + INDEX_PLUS
            else:
                max_len = max(max_len, i - start + INDEX_PLUS)

            used_map[c] = i

        return max_len
