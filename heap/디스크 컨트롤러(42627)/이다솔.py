def solution(jobs):
    time, now, jobs_num = 0, min(jobs)[0], len(jobs) # time = 요청시간, now = 현재 시간, jobs_num = 작업 개수
    while jobs :
        candidate = [jobs[i] for i in range(len(jobs)) if jobs[i][0] <= now] # 요청된 시각이 현재 시각보다 작은 작업
        if not candidate :                                                   # 공백 시간이 길어진 경우,
            now = min(jobs)[0]                                               # 현재 시각을 남은 작업의 요청 시각으로 변경
            continue
        candidate = sorted(candidate, key= lambda x : x[1])                  # 작업 소요 시간이 짧은 순으로 정렬
        jobs.remove(candidate[0])                                            # 가장 짧은 작업을 원래 리스트에서 삭제
        time += now + candidate[0][1] - candidate[0][0]                      # 현재 시각 + 작업 소요 시간 - 작업 시작 시각
        now += candidate[0][1]                                               # 현재 시각 업데이트

    return int(time / jobs_num)                                              # 평균 구해서 반환
