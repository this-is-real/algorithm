def check_positions(m,n,board):
    positions = []
    for i in range(n-1):
        for j in range(m-1):
            l_t = board[i][j]
            l_b = board[i+1][j]
            r_t = board[i][j+1]
            r_b = board[i+1][j+1]
            if (l_t == l_b == r_t == r_b) and l_t != '1' and l_t != '0':
                positions.append((i,j))
    return positions
def solution(m, n, board):
    board = [[s for s in item] for item in board]
    #transpose
    new_board = [ ['' for j in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            new_board[j][i] = board[i][j]
    positions = check_positions(m,n,new_board)
    count = 0
    while positions != []:
        for item in positions:
            i = item[0]
            j = item[1]
            new_board[i][j] = '1'
            new_board[i+1][j] = '1'
            new_board[i][j+1] = '1'
            new_board[i+1][j+1] = '1'
        result = []
        
        for col in new_board:
            new_col = []
            for item in col:
                if item != '1':
                    new_col.append(item)
                else :
                    new_col.insert(0,'0')
                    count += 1
            result.append(new_col)
        new_board = result
        positions = check_positions(m,n,result)
        
    answer = count
    return answer