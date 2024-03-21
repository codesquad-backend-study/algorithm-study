from collections import OrderedDict


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    queue = OrderedDict()
    time = 0

    for city in cities:
        city = city.lower()

        if city in queue:
            time += 1
            queue.move_to_end(city)
        else:
            if len(queue) >= cacheSize:
                queue.popitem(False)
            time += 5
            queue[city] = city

    return time
