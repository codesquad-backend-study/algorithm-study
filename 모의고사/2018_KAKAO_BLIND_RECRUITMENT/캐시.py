# LRU 캐시,
# cache hit = 1
# cache miss = 5
# 실행시간은?

import collections


def solution(cacheSize, cities):
    cache = collections.deque([])

    time = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            time += 5
    return time
