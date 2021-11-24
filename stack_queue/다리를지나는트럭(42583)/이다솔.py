def solution(bridge_length, weight, truck_weights):
    time = 0
    road = [0] * bridge_length
    while road :
        time += 1
        road.pop(0)
        if truck_weights :
            if sum(road) + truck_weights[0] <= weight :
                road.append(truck_weights.pop(0))
            else :
                road.append(0)
    return time 