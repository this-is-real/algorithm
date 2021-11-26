import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K:
            break
        elif len(scoville) <= 1:
            return -1
        
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        
        heapq.heappush(scoville, x+y*2)
        answer += 1
            
    return answer

