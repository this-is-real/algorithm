from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    answer = 0
    summed = sum(queue)
    
    while queue:
        answer += 1
        summed -= queue.popleft()
        
        if truck_weights:
            if truck_weights[0] + summed <= weight:
                temp = truck_weights.popleft()
                queue.append(temp)
                summed += temp
            else:
                queue.append(0)
    return answer
