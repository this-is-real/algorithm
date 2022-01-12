def get_time_str(time):
    hour, minute = divmod(time, 60)
    return f"{hour:02d}:{minute:02d}"

def solution(n, t, m, timetable):
    answer = ''
    
    new_timetable = []
    for tt in timetable:
        hour, minute = map(int, tt.split(":"))
        new_timetable.append(hour*60+minute)
    new_timetable = sorted(new_timetable)

    last_time, last_shuttle = 0, []
    for i in range(n):
        now_time = 9*60 + t*i
        indices = []
        for j, time in enumerate(new_timetable):
            if len(indices) < m:
                break
            if time <= now_time:
                indices.append(j)
        shuttle = [new_timetable[j] for j in indices]
        new_timetable = [time for j, time in enumerate(new_timetable) if j not in indices]
        last_time = now_time
        last_shuttle = shuttle

    if len(last_shuttle) < m:
        answer = get_time_str(last_time)
    else:
        answer = get_time_str(last_shuttle[-1]-1)
            
    return answer