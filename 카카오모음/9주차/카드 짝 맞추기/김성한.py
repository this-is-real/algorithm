from itertools import permutations
from collections import deque, defaultdict

size = 4
myboard = None
card_pos = defaultdict(list)
orders = []
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
INF = int(1e4)
answer = INF

def isin(y, x):
    return 0 <= x < size and 0 <= y < size
    
def move(y, x, yy, xx):
    global myboard
    ny, nx = y, x
    
    while True:
        _ny = ny + yy
        _nx = nx + xx
        if not isin(_ny, _nx):
            return ny, nx
        if myboard[_ny][_nx] != 0:
            return _ny, _nx
        ny, nx = _ny, _nx
            
    
def bfs(sy, sx, ey, ex):
    global myboard
    
    if [sy, sx] == [ey, ex]:
        return sy, sx, 1
    
    distance = [[0 for _ in range(size)] for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]
    queue = deque([[sy, sx]])
    visited[sy][sx] = True
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if isin(ny, nx):
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    if [ny, nx] == [ey, ex]:
                        return ny, nx, distance[ny][nx] + 1
                    queue.append([ny, nx])
    
            ny, nx = move(y, x, dy[i], dx[i])
        
            if not visited[ny][nx]:
                visited[ny][nx] = True
                distance[ny][nx] = distance[y][x] + 1
                if [ny, nx] == [ey, ex]:
                    return ny, nx, distance[ny][nx] + 1
                queue.append([ny, nx])
                
    return sy, sx, INF

def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = 0

def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = card

def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos
    
    if k == len(card_pos.keys()):
        if answer > count:
            answer = count
        return
    
    card = orders[m][k]
    y1, x1 = card_pos[card][0][0], card_pos[card][0][1]
    y2, x2 = card_pos[card][1][0], card_pos[card][1][1]
    
    ry1, rx1, res1 = bfs(sy, sx, y1, x1)
    ry2, rx2, res2 = bfs(ry1, rx1, y2, x2)
    
    remove(card)
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    restore(card)
    
    ry1, rx1, res1 = bfs(sy, sx, y2, x2)
    ry2, rx2, res2 = bfs(ry1, rx1, y1, x1)
    
    remove(card)
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    restore(card)
    
    
def solution(board, r, c):
    global myboard, card_pos, orders, answer
    
    myboard = board

    # make card_pos
    for i in range(size):
        for j in range(size):
            if myboard[i][j] != 0:
                card = myboard[i][j]
                card_pos[card].append([i, j])
    
    # make orders
    orders = list(permutations([key for key in card_pos.keys()]))
    
    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0) # sy, sx, k, m, count
    
    return answer