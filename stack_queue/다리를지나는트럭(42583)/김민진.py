def solution(bridge_length, weight, truck_weights):
    answer = 0
    # passing = deque([0] * bridge_length)
    passing = [0] * bridge_length

    while passing:
        answer += 1
        #passing.popleft()
        passing.pop(0)
        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)

    return answer