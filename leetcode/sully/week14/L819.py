from collections import defaultdict
from typing import List


class Solution:
    # 가장 많은 단어를 출력하는 문제
    # 대신 banned에 포함되어 있는 단어들은 제외함
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count_dic = defaultdict(int)
        split_paragraph = paragraph.replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(
            ';', ' ').replace(".", ' ').lower().split()

        # 맵 만들기
        for s in split_paragraph:
            count_dic[s] += 1

        while True:
            max_key = max(count_dic, key=count_dic.get)

            # 금지 단어가 포함이 안 되어 있으면 -> 그냥 리턴
            if max_key not in banned:
                return max_key

            # 금지 단어에 포함돼 있으먼 -> 다시 while문 돌면서 딕셔너리 제거
            count_dic.pop(max_key)


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
