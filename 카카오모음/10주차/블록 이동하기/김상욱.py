def solution(board):
    """
        STEP1. 보드를 만들고 10000 으로 넣어주기
        STEP2. 이동 케이스 별로 나눠서 구현하기 -> 가로(위아래좌우 + 오른쪽,왼쪽 * 위,아래), 세로(위아래좌우 + 위, 아래 * 오른쪽, 왼쪽)
        STEP3. 다익스트라로 최소값 적재하기
    """
    n = len(board)
    robot = [[[10000 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    robot[0][0][0] = 0
    
    queue = []
    queue.append([0,0,0])

    while queue:
        x, y, dir = queue.pop(0)
        depth = robot[x][y][dir]


        # 가로모양부터 모든 케이스 탐색
        if dir == 0:
            # 위
            if x != 0 and board[x-1][y] + board[x-1][y+1] == 0:
                if robot[x-1][y][dir] > depth+1:
                    robot[x-1][y][dir] = depth+1
                    queue.append([x-1, y, dir])
                # 회전축 기준
                # 왼쪽
                if robot[x-1][y][int(not dir)] > depth+1:
                    robot[x-1][y][int(not dir)] = depth+1
                    queue.append([x-1, y, int(not dir)])
                # 오른쪽
                if robot[x-1][y+1][int(not dir)] > depth+1:
                    robot[x-1][y+1][int(not dir)] = depth+1
                    queue.append([x-1, y+1, int(not dir)])
            # 아래
            if x != n-1 and board[x+1][y] + board[x+1][y+1] == 0:
                if robot[x+1][y][dir] > depth+1:
                    robot[x+1][y][dir] = depth+1
                    queue.append([x+1, y, dir])
                # 회전축 기준
                # 왼쪽
                if robot[x][y][int(not dir)] > depth+1:
                    robot[x][y][int(not dir)] = depth+1
                    queue.append([x, y, int(not dir)])
                # 오른쪽
                if robot[x][y+1][int(not dir)] > depth+1:
                    robot[x][y+1][int(not dir)] = depth+1
                    queue.append([x, y+1, int(not dir)])
            # 왼쪽
            if y != 0 and board[x][y-1] == 0:
                if robot[x][y-1][dir] > depth+1:
                    robot[x][y-1][dir] = depth+1
                    queue.append([x, y-1, dir])
            # 오른쪽
            if y != n-2 and board[x][y+2] == 0:
                if robot[x][y+1][dir] > depth+1:
                    robot[x][y+1][dir] = depth+1
                    queue.append([x, y+1, dir])
        # 세로 모양일때,
        else:
            # 위
            if x != 0 and board[x-1][y] == 0:
                if robot[x-1][y][dir] > depth+1:
                    robot[x-1][y][dir] = depth+1
                    queue.append([x-1, y, dir])
            # 아래
            if x != n-2 and board[x+2][y] == 0:
                if robot[x+1][y][dir] > depth+1:
                    robot[x+1][y][dir] = depth+1
                    queue.append([x+1, y, dir])
            # 왼쪽
            if y != 0 and board[x][y-1] + board[x+1][y-1] == 0:
                if robot[x][y-1][dir] > depth+1:
                    robot[x][y-1][dir] = depth+1
                    queue.append([x, y-1, dir])
                # 회전축 기준
                # 위
                if robot[x][y-1][int(not dir)] > depth+1:
                    robot[x][y-1][int(not dir)] = depth+1
                    queue.append([x, y-1, int(not dir)])
                # 아래
                if robot[x+1][y-1][int(not dir)] > depth+1:
                    robot[x+1][y-1][int(not dir)] = depth+1
                    queue.append([x+1, y-1, int(not dir)])
            # 오른쪽
            if y != n-1 and board[x][y+1] + board[x+1][y+1] == 0:
                if robot[x][y+1][dir] > depth+1:
                    robot[x][y+1][dir] = depth+1
                    queue.append([x, y+1, dir])
                # 회전축 기준
                # 위
                if robot[x][y][int(not dir)] > depth+1:
                    robot[x][y][int(not dir)] = depth+1
                    queue.append([x, y, int(not dir)])
                # 아래
                if robot[x+1][y][int(not dir)] > depth+1:
                    robot[x+1][y][int(not dir)] = depth+1
                    queue.append([x+1, y, int(not dir)])
    
    return min(robot[n-1][n-2][0], robot[n-2][n-1][1])