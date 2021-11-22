def solution(progresses, speeds):
    import math
    done = [math.ceil((100 - progresses[idx]) / speeds[idx]) for idx in range(len(progresses))]
    idx = 0
    release = []
    while True :
        feature = done[idx]
        for i in range(idx, len(done)) :
            if done[i] > feature :
                release.append(i - idx)
                idx = i
                break
        if i == len(done) - 1 :
            release.append(i - idx + 1)
            break   
    return release