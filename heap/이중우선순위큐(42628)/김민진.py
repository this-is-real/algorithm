import heapq

def solution(operations):
    min_heap = []
    heapq.heapify(min_heap)
    max_heap = []
    heapq.heapify(max_heap)
    
    for op in operations:
        command, data = op.split(" ")
        data = int(data)
        if command == "I":
            heapq.heappush(min_heap, data)
            heapq.heappush(max_heap, -data)
        else:
            if not min_heap:
                continue
            elif data == 1:
                min_heap.remove(-heapq.heappop(max_heap))
            elif data == -1:
                max_heap.remove(-heapq.heappop(min_heap))
                
    if not min_heap:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
        