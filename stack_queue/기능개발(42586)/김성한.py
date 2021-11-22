# 성공

import math

def solution(progresses, speeds):
    answer = []
    remain = [math.ceil((100 - p)/s) for p, s in zip(progresses, speeds)]
    while True:
        if sum(remain) == -1 * len(remain):
            break
        done_idx = []
        remain = [r-1 if r > 0 else r for r in remain]
        for i in range(len(remain)):
            if remain[i] == -1:
                continue
            elif remain[i] == 0:
                done_idx.append(i)
            elif remain[i] > 0:
                break
        if len(done_idx) > 0:
            answer.append(len(done_idx))
            remain = [-1 if i in done_idx else r for i, r in enumerate(remain)]
    return answer