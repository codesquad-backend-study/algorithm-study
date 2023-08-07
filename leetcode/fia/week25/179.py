from typing import List
from functools import cmp_to_key


class Solution:
    def comparator_by(self, a, b):
        a = str(a)
        b = str(b)

        for i in range(min(len(a), len(b))):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) == int(b[i]):
                continue
            elif int(a[i]) < int(b[i]):
                return -1

        if len(a) > len(b):
            if int(a[len(b)]) > int(b[-1]):
                return 1
            else:
                return -1
        elif len(b) > len(a):
            if int(b[len(a)]) > int(a[-1]):
                return -1
            else:
                return 1

        return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.comparator_by), reverse=True)
        return (''.join(map(str, nums)))
