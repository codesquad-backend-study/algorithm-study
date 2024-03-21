import collections
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:
    CACHE_HIT, CACHE_MISS = 1, 5
    answer = 0
    cache = collections.deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()

        if city in cache:
            answer += CACHE_HIT
            cache.remove(city)
        else:
            answer += CACHE_MISS

        cache.append(city)

    return answer
