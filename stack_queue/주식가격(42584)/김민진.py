def solution(prices):
    size = len(prices)
    answer = [0] * size
    for i in range(size-1):
        answer[i] += 1
        for j in range(i+1, size-1):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                break
    return answer