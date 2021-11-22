def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    bridge_weight = 0
    answer = 0

    while bridge:
        answer += 1
        done = bridge.pop(0)
        bridge_weight -= done

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                now = truck_weights.pop(0)
                bridge.append(now)
                bridge_weight += now
            else:
                bridge.append(0)

    return answer
