def solution(lines): 
    answer = 0 
    arr = [] 
    candidate = [] 
    for i in lines: 
        i = i.split()[1:] 
        time, T = i 
        T = float(T[:-1])
        end = int(time[0:2])*3600 + int(time[3:5])*60 + float(time[6:]) 
        start = end-T + 0.001 
        arr.append([start, end]) 
        candidate.append(end) 
    for i in candidate: 
        cnt = 0 
        for start, end in arr: 
            if start<i+1 and end >= i: 
                cnt += 1 
                answer = max(answer, cnt) 
    return answer
