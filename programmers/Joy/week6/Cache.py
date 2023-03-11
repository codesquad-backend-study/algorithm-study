def solution(cacheSize, cities):
    # 캐시 사이즈 = 0
    if cacheSize == 0 :
        return len(cities)*5

    cities = [i.lower() for i in cities]
    time = 0
    cache = []

    # cities 반복
    for i in cities:
        if i in cache:
            time += 1
            cache.remove(i)
            cache.append(i)
        else :
            time += 5
            if len(cache) == cacheSize:
                del cache[0]
                cache.append(i)
            else :
                cache.append(i)
    return time