def solution(N, stages):
    answer = {}
    num = len(stages)
    for i in range(1, N+1):
        if stages.count(i) != 0:
            answer[i] = stages.count(i)/num
            num -= stages.count(i)
        else:
            answer[i] = 0
    answer = sorted(answer, key=lambda x : answer[x], reverse=True)
    return answer
