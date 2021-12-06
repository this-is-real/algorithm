from collections import defaultdict, deque

def get_graph(tickets):
    graph = defaultdict(list)
    for s_city, d_city in tickets:
        graph[s_city].append(d_city)
    graph = {key: sorted(value) for key, value in graph.items()}
    return graph

def solution(tickets):
    graph = get_graph(tickets)
    
    stack = deque(["ICN"])
    answer = []
    while stack:
        city = stack[-1]
        if city not in graph.keys() or len(graph[city]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[city].pop(0))
    
    answer = answer[::-1]
    
    return answer