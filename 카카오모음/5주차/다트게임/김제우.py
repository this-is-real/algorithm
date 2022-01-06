import re
def solution(dartResult):
    dart_result = re.findall(r"[0-9]{1,2}[SDT*#]{1,2}",dartResult)
    splited_darts = []
    for dart in dart_result :
        number = re.findall(r"[0-9]{1,2}", dart)[0]
        area = re.findall(r"[SDT]",dart)[0]
        option = re.findall(r"[*#]",dart)
        if option :
            option = option[0]
        else :
            option = ""
        splited_darts.append([number,area,option])
    
    result = []
    for i,item in enumerate(splited_darts):
        temp_score = 0
        temp_score += int(item[0])
        if item[1] == "S":
            temp_score = temp_score**1
        elif item[1] == "D":
            temp_score = temp_score**2
        elif item[1] == "T":
            temp_score = temp_score**3
        if item[2] == "*":
            if i == 0:
                temp_score *= 2
            else :
                temp_score *= 2
                past_score = result.pop()
                result.append(past_score * 2)
        elif item[2] == "#":
            temp_score = -temp_score
        
        result.append(temp_score)    
            
                
    answer = sum(result)
    return answer