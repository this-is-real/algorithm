import heapq
def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for i in operations: # 숫자 넣기
        if 'I' in i:
            heapq.heappush(min_heap, int(i[1:]))
            heapq.heappush(max_heap, -int(i[1:]))
            
        elif i == 'D -1' and len(min_heap) != 0: # 최소값
            max_heap.remove(-heapq.heappop(min_heap))
            
        elif i == 'D 1' and len(max_heap) != 0: # 최대값
            min_heap.remove(-heapq.heappop(max_heap))
        
    if len(max_heap) == 0 or len(min_heap) == 0:
        return [0,0]
    
    answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    return answer
