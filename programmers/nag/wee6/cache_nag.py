def solution(cacheSize, cities):
    answer = 0
    log = []
    cache = []
    
    for index in range(len(cities)):
        cities[index] = cities[index].lower()
    print(cities)
    
    for city in cities:
        if cacheSize == 0:
            answer += 5
            continue
        if len(cache) < cacheSize:
            if city not in cache:
                cache.append(city)
                answer += 5
                continue
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1
                continue
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
        if not cache:
            cache.append(city)
        cache.pop(0)
        cache.append(city)
        answer += 5

    return answer
