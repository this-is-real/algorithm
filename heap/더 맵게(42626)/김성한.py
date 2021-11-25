# 성공

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        check = True
        for s in scoville:
            if s < K: # 일부를 탐색하게끔 로직을 변경하여 시간 초과 해결
                check = False
                break
        
        if check: break
        
        if len(scoville) == 1:
            answer = -1
            break
            
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_food = food1 + (food2 * 2)
        heapq.heappush(scoville, new_food)
        
        answer += 1
    return answer