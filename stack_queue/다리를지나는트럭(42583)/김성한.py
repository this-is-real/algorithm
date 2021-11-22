# 성공

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    #print(answer, bridge, truck_weights)
    while True:
        # 종료 조건
        if len(truck_weights) == 0 and len(bridge) == 0:
            break

        answer += 1
            
        # 다리를 다 건넌 트럭 확인
        if len(bridge) > 0:
            for i in range(len(bridge)):
                if bridge[i][1] == 1:
                    bridge.pop(i)
                    break
        
        # 다리 지나가기
        if len(bridge) > 0:
            for i in range(len(bridge)):
                bridge[i][1] -= 1

        # 다리 올라가기
        if len(truck_weights) > 0:
            wait_truck = truck_weights[0]
            bridge_weight = sum([truck[0] for truck in bridge]) if len(bridge) > 0 else 0
            if (weight - bridge_weight) >= wait_truck:
                bridge.append([truck_weights.pop(0), bridge_length])

        #print(answer, bridge, truck_weights)
    return answer

# 다른 풀이
def solution2(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    #print(time, bridge, truck_weights)
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            new_weight = 0 if sum(bridge) + truck_weights[0] > weight else truck_weights.pop(0)
            bridge.append(new_weight)
        #print(time, bridge, truck_weights)
    return time