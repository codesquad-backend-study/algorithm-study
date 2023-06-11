import collections
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = collections.Counter(nums)

    return [value[0] for value in counter.most_common(k)]
