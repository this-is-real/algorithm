def solution(board, moves):
    answer = 0
    bucket = []
    
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                bucket.append(b[m-1])
                b[m-1] = 0
                break
                
        if len(bucket)>=2 and bucket[-1]==bucket[-2]:
                bucket = bucket[:-2]
                answer += 2
                
    return answer
