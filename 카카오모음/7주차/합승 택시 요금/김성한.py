import heapq

graph = None

def dijkstra(start, end):
    global graph
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        
        if distances[cur_node] < cur_dist:
            continue
        
        for next_dist, next_node in graph[cur_node]:
            new_dist = cur_dist + next_dist
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(queue, [new_dist, next_node])
    
    return distances[end]

def solution(n, s, a, b, fares):
    global graph
    
    answer = float('inf')
    
    graph = {i+1: [] for i in range(n)}
    for node1, node2, dist in fares:
        graph[node1].append([dist, node2])
        graph[node2].append([dist, node1])
    
    for i in range(1, n+1):
        answer = min(answer, (dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)))
    
    return answer