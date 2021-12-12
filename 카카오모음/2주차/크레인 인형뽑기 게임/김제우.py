def solution(board, moves):
    board_size = len(board)
    box = []
    count = 0
    for move in moves:
        for i in range(board_size):
            item = board[i][move-1]
            if 0 == item :
                continue
            if box:
                if box[-1] == item :
                    count += 2
                    box.pop()
                else:
                    box.append(item)
            else:
                box.append(item)
            board[i][move-1] = 0
            break
    return count