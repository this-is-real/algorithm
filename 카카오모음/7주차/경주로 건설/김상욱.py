def solution(board):
    answer = float('inf')
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = []
    
    board[0][0] = 1

    if board[1][0] == 0:
        queue.append([1, 0, 100, True]) # x, y, cost, is_x
        board[1][0] = 1

    if board[0][1] == 0:
        queue.append([0, 1, 100, False])
        board[0][1] = 1
        
    while queue:
        nx, ny, cost, is_x = queue.pop(0)
        for i in range(4):
            nnx = nx + dx[i]
            nny = ny + dy[i]

            if 0 <= nnx < len(board) and 0 <= nny < len(board[0]):
                # 벽이 아니면
                if board[nnx][nny] != 1:
                    # 기존 진행방향과 동일하면
                    if (dx[i] and is_x) or (dy[i] and not is_x):
                        # 가려는 곳이 0이거나 지금 추가될 값보다 작거나 같다면
                        # 같은 값을 넣는 이유는 해당 지점에서 방향이 각기 다른 케이스 때문에 추가함
                        # 즉, is_x 값이 다를 수 있기에...
                        if board[nnx][nny] >= cost + 100 or board[nnx][nny] == 0:
                            board[nnx][nny] =  cost + 100
                            queue.append([nnx, nny, cost + 100, is_x])
                    # 기존 진행방향과 다르다면
                    else:
                        # 600원 기준이 아니라 100원 보다 큰 경우를 넣은 이유는?
                        # 지점에서 꺾여서 들어 간 값이 더 클 수 있지만 그 다음에 직진으로 인해 작아질수 있다.
                        # 그렇기에 직진으로 들어온 값보다 큰 케이스도 해당 값을 담아주도록 한다.
                        # 단 그 다음 케이스를 고려해도 의미가 없을 수 있다. 그 값이 100
                        if board[nnx][nny] > cost + 100 or board[nnx][nny] == 0:
                            board[nnx][nny] = cost + 600
                            queue.append([nnx, nny, cost + 600, not is_x])
                            
            if nnx == len(board) - 1 and nny == len(board[0]):
                answer = min(answer, board[-1][-1])
    
    return answer