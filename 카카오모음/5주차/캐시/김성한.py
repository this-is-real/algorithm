def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city not in cache: # miss
            answer += 5
            if cacheSize == 0:
                continue
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else: # hit
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
    return answer