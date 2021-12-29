import itertools
import re

# unsolved
def solution(s):
    answer = 0    
    operations = re.findall(r'[-*+]', s)
    
    for order in itertools.permutations(set(operations)):
        temp = s
        for ind,oper in enumerate(order):
            if ind == len(order)-1:
                temp = eval(temp)
                break
            else:
                match = re.findall(f"\d+\{oper}\d+", temp)
                # match = re.findall(f".\d+\{oper}.\d+|\d+\{oper}\d+", temp)
                for m in match:
                    # if m[0] != '-' and m[0] != '0-9': m = m[1:]
                    temp = temp.replace(m,str(eval(m)))
        answer = max(answer, abs(temp))
    return answer