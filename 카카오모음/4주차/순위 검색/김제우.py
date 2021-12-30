import re
from collections import defaultdict
def solution(info, query):
    scores = []
    table = defaultdict(list)
    for i,person in enumerate(info):
        info_list = person.split()
        table[info_list[0]].append(i)
        table[info_list[1]].append(i)
        table[info_list[2]].append(i)
        table[info_list[3]].append(i)
        scores.append(int(info_list[4]))
        
    conditions = []
    for q in query:
        q = re.sub(r'(and)','',q)
        q = q.split()
        conditions.append(q)
        
    result = []
    for condition in conditions:
        lang, work, career, food = set(),set(),set(),set()
        if condition[0] == "-":
            lang = set(range(len(info)))
        else :
            lang = set(table[condition[0]])
        
        if condition[1] == "-":
            work = set(range(len(info)))
        else :
            work = set(table[condition[1]])
            
        if condition[2] == "-":
            career = set(range(len(info)))
        else :
            career = set(table[condition[2]])
            
        if condition[3] == "-":
            food = set(range(len(info)))
        else :
            food = set(table[condition[3]])
        ans = list(lang & work & career & food)
        i = 0
        if condition[4] == "-":
            i = len(ans)
        else :
            for person in ans:           
                if scores[person] >= int(condition[4]):
                    i += 1
        result.append(i)   
    
    answer = result
    return answer