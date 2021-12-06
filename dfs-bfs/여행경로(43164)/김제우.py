# def bfs(graph,start,ticket_num):
#     queue = [(start,[start])]
#     visited = []
    
#     while queue:
#         node,path = queue.pop(0)
#         if len(path) == ticket_num:
#             visited.append()
#         if node in graph:
#             for m in set(graph[node])-set(path):
#                 queue.append((m,path+[m]))
#                 print(queue)
def dfs(graph, start):
    stack = [start]
    visited = []
    
    while stack:
        node = stack.pop()
        if node not in graph:
            visited.append(node)
        else :
            stack.extend(graph[node])
    print(visited)
        # for item in set(graph[node])-set(path):
        #     if item in graph and item not in visited:
        #         stack.extend([(item,path+[item])])
        #         print(stack)
    
def solution(tickets):
    ticket_num = len(tickets)
    graph = {}
    for ticket in tickets:
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else :
            graph[ticket[0]].append(ticket[1])
    graph = {key:sorted(value) for key, value in graph.items()}
    print(graph)
    # bfs(graph,'ICN',ticket_num)
    dfs(graph,'ICN')
    
    answer = []
    return answer