import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for s in strs:
            # key: 정렬된 문자열, value: 기존 문자열 리스트
            # 즉, 정렬된 문자열인 key값이 같으면 value에 계속 append가 되는 형식
            dic[''.join(sorted(s))].append(s)

        return list(dic.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
