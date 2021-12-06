def solution(tickets):
    tickets = sorted(tickets, reverse=True)
    routes = dict()
    answer = []
    for s, e in tickets :
        if s in routes :
            routes[s].append(e)
        else :
            routes[s] = [e]
    plan = ['ICN']
    while plan :
        now = plan[-1]
        if now not in routes or len(routes[now]) == 0 :
            answer.append(plan.pop())
        else :
            plan.append(routes[now].pop())
    answer.reverse()
    return answer
