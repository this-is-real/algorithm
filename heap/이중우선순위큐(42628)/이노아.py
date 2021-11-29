import heapq

def solution(operations):
    min_heap, max_heap = [],[]
    for i in operations:
        if (i == 'D 1' or i == 'D -1') and (len(min_heap) == 0):
            pass
        
        elif i == 'D 1':
            min_heap.remove(-heapq.heappop(max_heap))
        
        elif i == 'D -1':
            max_heap.remove(-heapq.heappop(min_heap))
        
        else:
            temp = int(i.split()[1])
            heapq.heappush(min_heap, temp)
            heapq.heappush(max_heap, -temp)
    
    if len(min_heap) == 0:
        return [0,0]
    
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]