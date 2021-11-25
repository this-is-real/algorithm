def solution(brown, yellow):
    t = brown + yellow
    cand = []
    for i in range(t-1,0,-1): # 노란 타일 한줄 불가
        if t % i == 0:        
            if i < t//i:      # 가로 >= 세로
                break
            cand.append([i,t//i])

    return [c for c in cand if (c[0]-2)*(c[1]-2) == yellow][0]
