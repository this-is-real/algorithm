def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for per_idx, per in enumerate([a,b,c]):
        for q_i in range(len(answers)):
            if answers[q_i] == per[q_i % len(per)]:
                score[per_idx] += 1
                
    return [ind+1 for ind,s in enumerate(score) if s == max(score)]
