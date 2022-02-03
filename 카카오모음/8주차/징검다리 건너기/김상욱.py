def solution(stones, k):
    """
        idea1: 한명씩 이동시키고, stone - 1 업데이트, 0이 반복적으로 k번 나오면 stop -> 효율성에서 안됨
        idea2: min(stones)만큼 이동시키고 stone - min(stones) 업데이트 -> 효율성에서 안됨
        idea3: 윈도우를 k개로 주고, 슬라이드 하면서 min(max(window))로 찾는 방법 -> 효율성에서 안됨
        idea4: 이분법 사용...
    """
    left = 1
    right = max(stones)

    while left <= right:
        stones_temp = stones.copy()
        mid = (left + right) // 2
        step = 0

        for stone in stones_temp:
            if stone - mid <= 0:
                step += 1
            else:
                step = 0

            if step >= k:
                break

        if step >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left
