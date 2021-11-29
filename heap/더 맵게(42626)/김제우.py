import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville :
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        first = heapq.heappop(scoville)
        if first >= K :
            return answer
        second = heapq.heappop(scoville)
        new_scov = first + second *2
        heapq.heappush(scoville, new_scov)
        answer += 1