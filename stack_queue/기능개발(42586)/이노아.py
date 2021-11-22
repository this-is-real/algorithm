from collections import deque

def solution(progresses, speeds):
    answer = []
    zipped  = deque(list(zip(progresses, speeds)))
    count, time = 0,0
    
    while len(zipped)> 0:
        if (zipped[0][0] + time*zipped[0][1]) >= 100:
            zipped.popleft()
            count +=1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)
    return answer
