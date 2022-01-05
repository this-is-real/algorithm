import re

def get_play_time(s_time, e_time):
    s_h, s_m = map(int, s_time.split(":"))
    e_h, e_m = map(int, e_time.split(":"))
    return (e_h - s_h) * 60 - s_m + e_m

def split_score(score):
    return re.findall(r"[A-G]{1}#*", score)
        
    
def solution(m, musicinfos):
    answer = []
    
    for musicinfo in musicinfos:
        s_time, e_time, title, score = musicinfo.split(",") # score: 악보
        
        play_time = get_play_time(s_time, e_time)

        score = split_score(score)
        full_score = score * ((play_time // len(score)) + 1)
        full_score = full_score[:play_time]
        
        music = split_score(m)

        is_match = False
        for i in range(len(full_score)):
            if full_score[i:i+len(music)] == music:
                is_match = True
                break
        
        if is_match:
            answer.append((title, play_time))
    
    if answer:
        answer = sorted(answer, key=lambda x: -x[1])
        return answer[0][0]
    else:
        return "(None)"