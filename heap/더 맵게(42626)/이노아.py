import heapq

def solution(scoville, k):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if heap[0] >= k: # first node min (min heap)
            break
        elif len(heap) <= 1:
            return -1
        
        # pop top2
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        heapq.heappush(heap, min1 + min2*2)
        answer += 1
        
    return answer