# heapq안씀ㅜㅜ

def solution(jobs):
    answer = 0
    now = 0
    s_jobs = sorted(jobs, key=lambda x:x[1]) # 소요시간 순 정렬
    
    while s_jobs:
        for i in range(len(s_jobs)):
            if s_jobs[i][0] <= now:
                now += s_jobs[i][1]
                answer += now - s_jobs[i][0]
                s_jobs.pop(i)
                break
            elif i == len(s_jobs)-1:
                now += 1
    return  answer // len(jobs)
