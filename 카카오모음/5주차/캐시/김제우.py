#30분
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    cities = [item.lower() for item in cities]
    run_time = 0
    cache = []
    start_index = 0
    for i,city in enumerate(cities):
        if len(cache) == cacheSize:
            start_index = i
            break
        if city not in cache:
            cache.append(city)
            run_time += 5
        else :
            run_time += 1
            cache.remove(city)
            cache.append(city)
    cities = cities[start_index:]

    while cities:
        input_data = cities.pop(0)
        if input_data in cache:
            run_time+=1
            cache.remove(input_data)
            cache.append(input_data)
        else :
            run_time+=5
            cache = cache[1:]
            cache.append(input_data)
            
    answer = run_time
    return answer