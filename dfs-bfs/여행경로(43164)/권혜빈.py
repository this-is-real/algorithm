from collections import defaultdict

def solution(tickets): 
    def dfs(start): 
        while lists[start]: 
            dfs(lists[start].pop(0)) 
        answer.append(start)
    
    answer = [] 
    lists = defaultdict(list) 
    for start, arrv in sorted(tickets): 
        lists[start].append(arrv) 
        
    dfs('ICN')
    return answer[::-1]
