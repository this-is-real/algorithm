def str_to_int(time):
    h,m,s=time.split(':')
    return int(h)*3600+int(m)*60+int(s)

def int_to_str(time):
    h = time // 3600
    time = time%3600
    m = time // 60
    s = time - m * 60
    return str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    answer = ''
    
    # 초로 바꾸기
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    
    user = [0 for i in range(play_time + 1)]
    
    for i in logs:
        start, end = map(str, i.split('-'))
        start = str_to_int(start)
        end = str_to_int(end)

        user[start] += 1
        user[end] -= 1
        
    for i in range(1, play_time+1):
        user[i] = user[i]+user[i-1]
    for i in range(1, play_time+1):
        user[i] = user[i]+user[i-1]
        
        
    max_play = user[adv_time-1]
    start = 0
    
    for i in range(adv_time, play_time):
        play = user[i]-user[i-adv_time]
        if play>max_play:
            max_play = play
            start = i-adv_time+1
    answer = int_to_str(start)
    
    return answer