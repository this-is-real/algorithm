from collections import deque

def solution(board):
    n = len(board)
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
    directions = ["vertical", "vertical", "horizontal", "horizontal"]
    
    costs = [[[float('inf') for _ in range(n)] for _ in range(n)] for _ in range(4)]
    queue = deque([[0, 0, 0, ""]])
    
    while queue:
        x, y, cost, direction = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                new_cost = 100 if direction == "" or direction == directions[i] else 600
                if costs[i][nx][ny] > cost + new_cost:
                    costs[i][nx][ny] = cost + new_cost
                    queue.append([nx, ny, cost + new_cost, directions[i]])
    
    return min([cost[-1][-1] for cost in costs])