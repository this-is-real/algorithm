from collections import deque

def solution(priorities, location):
    zipped = deque(list(enumerate(priorities)))
    answer = []
    while True:
        if zipped[0][1] >= max(list(zipped)[1:], key = lambda t: t[1])[1]:
            ind,_ = zipped.popleft()
            answer.append(ind)
            
            if len(zipped) == 1:
                answer.append(zipped[0][0])
                break
                
        else:
            temp = zipped.popleft()
            zipped.append(temp)
            
    return answer.index(location)+1
