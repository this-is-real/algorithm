def solution(participant, completion):
    check={}
    
    for i in participant :
        check[i] = 0
    for i in participant :
        check[i] += 1
    for i in completion : 
        check[i] -= 1
    for i in check:
        if check[i] != 0 : answer = i
    return answer
