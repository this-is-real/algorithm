from collections import deque

def get_extended_board(board, n):
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    return new_board

def get_next_pos(pos, board):
    next_pos = []
    (x1, y1), (x2, y2) = pos
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    # 1. 상하좌우
    for i in range(4):
        xx1, yy1 = x1 + dx[i], y1 + dy[i]
        xx2, yy2 = x2 + dx[i], y2 + dy[i]
        if board[xx1][yy1] == 0 and board[xx2][yy2] == 0:
            next_pos.append({(xx1, yy1), (xx2, yy2)})
    
    # 2. 가로 -> 세로 회전
    if x1 == x2:
        for i in [-1, 1]:
            xx1 = x1 + i
            xx2 = x2 + i
            if board[xx1][y1] == 0 and board[xx2][y2] == 0:
                next_pos.append({(x1, y1), (xx1, y1)})
                next_pos.append({(x2, y2), (xx2, y2)})
                
    # 3. 세로 -> 가로 회전
    if y1 == y2:
        for i in [-1, 1]:
            yy1 = y1 + i
            yy2 = y2 + i
            if board[x1][yy1] == 0 and board[x2][yy2] == 0:
                next_pos.append({(x1, y1), (x1, yy1)})
                next_pos.append({(x2, y2), (x2, yy2)})
    
    return next_pos

def solution(board):
    answer = 0
    
    n = len(board)
    ext_board = get_extended_board(board, n)
    
    pos = {(1,1), (1,2)}
    visited = []
    queue = deque([(pos, 0)])
    visited.append(pos)
    
    while queue:
        new_pos, cost = queue.popleft()
        
        if (n, n) in new_pos:
            answer = cost
            break
        
        for next_pos in get_next_pos(new_pos, ext_board):
            if next_pos not in visited:
                visited.append(next_pos)
                queue.append((next_pos, cost+1))

    return answer