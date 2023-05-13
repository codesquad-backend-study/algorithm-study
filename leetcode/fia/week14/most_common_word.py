import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.findall('\\w+', paragraph)
        words = collections.defaultdict(int)

        for word in paragraph:
            word = word.lower()
            if word not in banned:
                words[word] = words[word] + 1

        return max(words, key=words.get)
