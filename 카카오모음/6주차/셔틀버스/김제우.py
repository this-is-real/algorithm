def solution(n, t, m, timetable):
    new_time_table = []
    start = 9*60
    for time in timetable:
        new_time_table.append(int(time.split(':')[0])*60 + int(time.split(':')[1]))
        
    new_time_table = sorted(new_time_table)
    bus_time_table = {}
    for i in range(start,start+t*n,t):
        m_count = m
        tmp_bus = []
        for item in new_time_table:
            if m_count == 0:
                break
            person = item
            if person <= i:
                tmp_bus.append(person)
            m_count -= 1
        new_time_table = new_time_table[len(tmp_bus):]
        bus_time_table[i] = tmp_bus
    
    last_bus = sorted(bus_time_table.keys(), reverse=True)[0]
    last_bus_people = bus_time_table[last_bus]
    result = 0
    if len(last_bus_people) != m :
        result = last_bus
    else :
        result = last_bus_people[-1]-1
        
    answer = str(result//60).rjust(2,'0') + ':' + str(result%60).rjust(2,'0')
    return answer