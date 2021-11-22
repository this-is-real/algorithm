import math

def solution(progresses, speeds):
    # 7/1 = 7 90/30 = 3, 45/5=9
    # 걸리는 날짜

    time = []
    for i, j in zip(progresses, speeds):
        if len(time) == 0 or math.ceil((100-i)/j) > time[-1][0]:
            time.append([math.ceil((100-i)/j), 1])
        else:
            time[-1][1] += 1
            
    answer = [i[1] for i in time]
    
    return answer
