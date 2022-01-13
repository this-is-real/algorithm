def solution(n, t, m, timetable):
    answer = 0
    people = [int(time[:2])*60 + int(time[3:]) for time in timetable] # 분으로 환산
    people.sort() # 정렬
    bus_time = [9*60 + t*i for i in range(n)] # 버스 도착시간 list
    
    i = 0
    for t in bus_time: 
        cnt = 0
        while cnt < m and i < len(people) and people[i] <= t: 
            i += 1 
            cnt += 1 
            if cnt < m: 
                answer = t
            else: answer = people[i-1] - 1 
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
