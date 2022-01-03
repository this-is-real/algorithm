def solution(m, n, board):
    board = [[i for i in j] for j in board]
    cnt = 0
    result = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    result.add((i,j))
                    result.add((i+1,j))
                    result.add((i,j+1))
                    result.add((i+1,j+1))

        if result:
            cnt += len(result)
            for i,j in result:
                board[i][j] = []
            result = set()
        else:
            return cnt
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
