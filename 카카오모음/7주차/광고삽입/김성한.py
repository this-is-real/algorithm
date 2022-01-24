def time2sec(time):
    hour, minute, second = map(int, time.split(":"))
    return hour*60*60 + minute*60 + second

def sec2time(sec):
    hour_minute, second = divmod(sec, 60)
    hour, minute = divmod(hour_minute, 60)
    return f"{hour:02d}:{minute:02d}:{second:02d}"
    

def solution(play_time, adv_time, logs):
    # STEP 1
    play_time_sec = time2sec(play_time)
    adv_time_sec = time2sec(adv_time)
    
    # STEP 2: 초 단위 시청자수 기록
    total_time = [0 for _ in range(play_time_sec+1)]
    for log in logs:
        start_sec, end_sec = map(time2sec, log.split("-"))
        total_time[start_sec] += 1
        total_time[end_sec] -= 1
    
    # STEP 3: 구간별 시청자수 기록
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
        
    # STEP 4: 구간별 누적 시청자수 기록
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
    
    # STEP 5: 가장 시청자수가 많은 구간 탐색
    most_view, max_time = 0, 0
    for i in range(adv_time_sec-1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i-adv_time_sec]:
                most_view = total_time[i] - total_time[i-adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1
    
    return sec2time(max_time)