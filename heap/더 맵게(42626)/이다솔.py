def solution(scoville, K):
    import heapq
    scoville.sort()
    times = 0
    heapq.heapify(scoville)

    while scoville[0] < K :
        dish = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, dish)
        times += 1
        
        if len(scoville) == 1 and scoville[0] < K :
            times = -1
            break
            
    return times
