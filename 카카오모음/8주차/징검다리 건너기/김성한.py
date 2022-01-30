def solution(stones, k):
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for stone in stones:
            if count == k:
                break
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
        if count < k:
            start = mid + 1
        else:
            end = mid - 1
    return start