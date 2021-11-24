def solution(answers):
    answer = []
    # 5 8 10 최소공만큼
    
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]        

    # a1
    for i in range(len(answers)):
            if a1[i%len(a1)] == answers[i] :
                count[0] += 1
    #a2
            if a2[i%len(a2)] == answers[i] :
                count[1] += 1
    #a3
            if a3[i%len(a3)] == answers[i] :
                count[2] += 1
    
    # 제일 많이 맞춘 수 answer에 넣기
    m = max(count)
    
    for i in range(3):
        if count[i] == m:
            answer.append(i+1)

    return answer
