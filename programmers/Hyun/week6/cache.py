import collections


def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    buf = collections.deque([])
    runtime = 0

    for city in cities:
        if city not in buf:
            runtime += 5
            if cacheSize > 0 and len(buf) == cacheSize:
                buf.popleft()
            if cacheSize > 0:
                buf.append(city)
        else:
            runtime += 1
            buf.remove(city)
            buf.append(city)

    return runtime
