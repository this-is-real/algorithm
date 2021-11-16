def solution(participant, completion):
    dict2 = {}
    for item in participant:
        if item not in dict2.keys() :
            dict2[item] = 1
        else :
            dict2[item] += 1
    for item in completion:
        dict2[item] -= 1
    
    for k, v in dict2.items():
        if v == 1:
            answer = k
            
    return answer