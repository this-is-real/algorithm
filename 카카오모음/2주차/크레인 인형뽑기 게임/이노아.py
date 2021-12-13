def solution(board, moves):
    stacked = [0]
    answer = 0
    for column in moves:
        for row,_ in enumerate(board):
            if board[row][column-1] > 0:
                if stacked[-1] == board[row][column-1]:
                    stacked.pop()
                    answer += 2
                else:
                    stacked.append(board[row][column-1])
                board[row][column-1] = 0
                break
    return answer