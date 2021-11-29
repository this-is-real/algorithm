import heapq
def solution(operations):
    operations = [item.split() for item in operations]
    operations = [[item[0],int(item[1])] for item in operations]
    max_heap= []
    min_heap= []
    for command, number in operations:
        if command == 'I':
            heapq.heappush(min_heap,number)
            heapq.heappush(max_heap,(-number, number))
        elif command == 'D':
            if number == -1 and max_heap and min_heap:
                target = heapq.heappop(min_heap)
                max_heap.remove((-target,target))
                
            elif number == 1 and max_heap and min_heap:
                min_heap.remove(heapq.heappop(max_heap)[1])

    if min_heap == []:
        return [0,0]
    else :
        return (max(min_heap),min(min_heap))