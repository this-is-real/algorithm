def dfs(visit, n, idx):
    visit[idx][0] = 1 # visit[idx] False -> True
    
    # 해당 node의 connected list 중 탐색할 곳 (cond1,2,3) 확인 후에 추가 탐색
    for i in range(n):
        if (visit[idx][1][i] == 1) and (visit[i][0] == 0):
            dfs(visit, n, i) # 조건 충족하는 다음 node에 대한 재귀적 적용

def solution(n, computers):
    visit =  list(map(list, zip([0]*n,computers))) # visit[0] -> [0, [0,0,0]] 형태
    answer = 0
    
    for idx in range(n):       # 모든 node에 대한 탐색
        if visit[idx][0] == 0: # 탐색 안한 node
            dfs(visit,n,idx)   # dfs 로 추가 탐색 필요한 경우 탐색
            answer += 1        # dfs 한번 끝날 때마다 answer += 1
    return answer