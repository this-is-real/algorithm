def solution(N, stages):
    fail  = []
    users = len(stages)
    for stage in range(1, N + 1) :
        loser = stages.count(stage)
        fail.append((stage, loser / users if users != 0 else 0))
        users -= loser
    fail = sorted(fail, key= lambda x : x[1], reverse=True)
    return [user[0] for user in fail]
