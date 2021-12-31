def remove(m, n, board, visited):
    dx, dy = [0, 0, 1, 1], [0, 1, 0, 1]
    for x in range(m-1):
        for y in range(n-1):
            is_target = True
            block = board[x][y]
            if block == "-": continue
            for z in range(4):
                xx, yy = x+dx[z], y+dy[z]
                if board[xx][yy] != block:
                    is_target = False
                    break
            if is_target:
                for z in range(4):
                    visited[x+dx[z]][y+dy[z]] = True

def move(m, n, board, visited):
    new_board = [["-" for _ in range(n)] for _ in range(m)]
    for j in range(n):
        temp = []
        for i in range(m):
            if not visited[i][j]:
                temp.append(board[i][j])
        for k, i in enumerate(range(m-len(temp), m)): # 핵심 포인트
            new_board[i][j] = temp[k]
    return new_board
                    
def solution(m, n, board):
    answer = 0
    #board = [list(row) for row in board]
    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]
        remove(m, n, board, visited)
        remove_cnt = sum([1 for i in range(m) for j in range(n) if visited[i][j]])
        if remove_cnt == 0: break
        answer += remove_cnt
        board = move(m, n, board, visited)        
    return answer