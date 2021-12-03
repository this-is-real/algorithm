def solution(n, computers):
    
    def dfs(i):
        total[i] = 1 
        for x in range(n):
            if computers[i][x]==1 and total[x]==0:
                dfs(x) 
                
    answer = 0
    total = [0]*n
    
    for i in range(n):
        if total[i]==0:
            dfs(i)
            answer += 1
    
    return answer
