def solution(prices):
    times = []
    for idx in range(len(prices)) :
        time = 0
        for idx2 in range(idx + 1, len(prices)) :
            time += 1
            if prices[idx] > prices[idx2] :
                break
        times.append(time)
    return times