def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll == 0:
                continue
            if bucket and doll == bucket[-1]:
                answer += 2
                bucket.pop()
            else:
                bucket.append(doll)
            board[i][move-1] = 0
            break
    return answer