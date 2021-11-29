# 성공

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    for i, operation in enumerate(operations):
        cmd, num = operation.split(" ")
        if cmd == "I":
            num = int(num)
            heapq.heappush(min_heap, (num, num))
            heapq.heappush(max_heap, (-1*num, num))
        elif cmd == "D":
            if len(min_heap) == 0:
                continue
            if num == "1":
                max_val = heapq.heappop(max_heap)
                min_heap.remove((-1*max_val[0], max_val[1]))
            elif num == "-1":
                min_val = heapq.heappop(min_heap)
                max_heap.remove((-1*min_val[0], min_val[1]))
    
    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]
    else:
        return [0, 0]