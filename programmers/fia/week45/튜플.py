import re
from collections import Counter


def solution(s):
    counter = Counter(re.findall('[0-9]+', s))

    return [int(key) for key, value in sorted(counter.items(), key=lambda x: -x[1])]
