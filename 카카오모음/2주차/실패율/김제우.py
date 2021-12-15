def solution(N, stages):
    fails = {i+1:0 for i in range(N)}
    succeses = {i+1:0 for i in range(N) }
    for stage in stages:
        if stage == N+1 :
            for i in range(1,stage):
                succeses[i] += 1
        else:
            fails[stage] += 1
            for i in range(1,stage):
                succeses[i] += 1
    result = []
    for i in range(1,N+1):
        if succeses[i] + fails[i] != 0:
            result.append((i,fails[i] / (succeses[i] + fails[i])))
        else :
            result.append((i,0))
    result = [i[0] for i in sorted(result, key = lambda x : x[1], reverse=True)]
    answer = result
    return answer