import heapq

def solution(jobs):
    jobs = [[b,a] for a,b in jobs]
    jobs = sorted(jobs, key = lambda t: (t[1], t[0]), reverse = True)
    heap = []
    n = len(jobs)
    answer = 0
    
    while True:
        if heap:
            time,start_ = heapq.heappop(heap)
            answer += time + (start - start_)
            start += time
        
        else:
            if not jobs:
                break
            else:
                time, start_ = jobs.pop()
                start = start_ + time
                answer += time
        
        if jobs:
            temp = []
            for j in jobs:
                if j[1] < start:
                    heapq.heappush(heap, j)
                    temp.append(j)
            for i in temp:
                jobs.remove(i)  # 위 for loop에서 제거 시 index 오류 발생
                                # + 매번 n개씩 탐색 비효율
        
    return answer // n