def solution(answers):
    per1 = [1,2,3,4,5]
    per2 = [2,1,2,3,2,4,2,5]
    per3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    per2_count = 0
    per3_count = 0
    
    for i in range(len(answers)):
        if per1[i%5] == answers[i] : 
            count[0] += 1
        if per2[i%8] == answers[i]:
            count[1] += 1
        if per3[i%10] == answers[i]:
            count[2] += 1
            
    answer = []
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
    return answer