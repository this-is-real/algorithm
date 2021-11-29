# 풀이 실패
def solution(jobs):
    job_length = len(jobs)
    answer = 0
    process = []
    time = 0
    jobs = sorted(jobs, key = lambda x : x[0])
    process.append(jobs.pop(0))
    time += process.pop(0)[1]
    
    while jobs:
        temp = []
        for job in jobs:
            if job[0] <= time :
                temp.append(job)
        selected_job = sorted(temp,key = lambda x : x[1])[0]
        process.append(selected_job)
        a = process.pop(0)
        time += time + a[1] - a[0]
        jobs.remove(selected_job)
    answer = (time-1)//job_length

# 요청 시작 시간 비교하기
# 요청 시작으로 부터 걸리는 총 시간 저장하기
# 프로세스 안에서 제일 짧은것 부터 넣기
    return answer