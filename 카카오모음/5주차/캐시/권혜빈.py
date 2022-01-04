def solution(cacheSize, cities):
    answer = 0
    now = []
    if cacheSize == 0 : return len(cities)*5
    for i in cities:
        i = i.lower()
        if i in now:
            answer += 1
            now.remove(i)
            now.append(i)
        else:
            answer += 5
            if len(now) < cacheSize:
                now.append(i)
            else:
                now.append(i)
                now = now[1:]
    return answer
