'''
풀이 못함. (다시 풀어서 업로드 예정)
'''

def solution(bridge_length, weight, truck_weights):
    total_time = 0
    passed = []
    on_bridge = []
    wait = [(item,0) for item in truck_weights]
    while len(passed) < len(truck_weights):
        wait_first = wait.pop(0)
        while True:
            on_bridge_weight = [weight for (_,weight) in on_bridge]
            if wait_first[0] + sum(on_bridge_weight) <= weight :
                on_bridge.append(wait_first)
                for (truck,timer) in on_bridge:
                    timer += 1
                    total_time += 1
                    break
            else :
                for (truck,timer) in on_bridge:
                    timer += weight - on_bridge[0][1]
                    total_time += weight - on_bridge[0][1]
            if on_bridge[0][1] >= bridge_length:
                passed.append(on_bridge.pop(0))
    print(total_time)
    answer = 0
    return answer