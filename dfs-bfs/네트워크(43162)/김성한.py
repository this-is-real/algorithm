# bfs

from collections import deque

def bfs(computers, n, visited, idx):
    queue = deque([])
    queue.append(idx)
    while queue:
        i = queue.popleft()
        visited[i] = True
        for j in range(n):
            if not visited[j] and computers[i][j] == 1:
                queue.append(j)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(computers, n, visited, i)
            answer += 1 # 연결된 모든 컴퓨터를 방문하는 bfs를 수행하면 하나의 네트워크가 생긴 것이다.
    return answer


# dfs

def dfs(computers, n, visited, idx):
    visited[idx] = True
    for j in range(n):
        if not visited[j] and computers[idx][j] == 1:
            dfs(computers, n, visited, j)
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(computers, n, visited, i)
            answer += 1 # 연결된 모든 컴퓨터를 방문하는 dfs를 수행하면 하나의 네트워크가 생긴 것이다.
    return answer