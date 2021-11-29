# 성공

import heapq

def solution(jobs):
    acc = 0         # 전체 작업시간
    s_time = -1     # 이전 작업 종료시간
    n_time = 0      # 현재시간
    completed = 0   # 완료된 작업 갯수
    heap = []
    while True:
        if completed == len(jobs):
            break
        for job in jobs:
            if s_time < job[0] <= n_time:
                heapq.heappush(heap, [job[1], job[0]]) # (작업소요시간, 작업요청시점)
        if len(heap):
            work = heapq.heappop(heap)
            s_time = n_time
            n_time += work[0]
            acc += n_time - work[1]
            completed += 1
        else:
            n_time += 1
    return acc // len(jobs)