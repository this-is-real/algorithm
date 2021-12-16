def solution(N, stages):  
    rate = [0]*N
    for i in range(N):
        if i+1 in stages:
            fail_cnt = sum([1 for x in stages if x == i+1])
            round_cnt = sum([1 for x in stages if x >= i+1])
            rate[i] = fail_cnt/round_cnt
    rate_sorted = sorted(list(enumerate(rate,1)), reverse = True, key = lambda t: t[1])
    return [ind for ind,_ in rate_sorted]