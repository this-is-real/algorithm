import re

def solution(dartResult):
    result = re.findall(r"(\d+)([SDT]{1})([*#]*)", dartResult)
    scores = [int(res[0]) for res in result]
    
    for i in range(len(scores)):
        _, bonus, option = result[i]
        
        if bonus == "S":
            scores[i] = scores[i]**1
        elif bonus == "D":
            scores[i] = scores[i]**2
        elif bonus == "T":
            scores[i] = scores[i]**3
        
        if option == "*":
            if i > 0:
                scores[i-1] = scores[i-1]*2
            scores[i] = scores[i]*2
        elif option == "#":
            scores[i] = scores[i]*(-1)
            
    return sum(scores)