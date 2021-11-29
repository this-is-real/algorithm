# DFS 풀이

answer = 0

def dfs(idx, result, numbers, target):
    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
    else:
        dfs(idx + 1, result + numbers[idx], numbers, target)
        dfs(idx + 1, result - numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer


# BFS 풀이

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0)) # idx, accumulate
    while queue:
        idx, acc = queue.popleft()
        if idx == len(numbers):
            if acc == target:
                answer += 1
        else:
            queue.append((idx+1, acc + numbers[idx]))
            queue.append((idx+1, acc - numbers[idx]))
    return answer