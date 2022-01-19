from collections import defaultdict
import heapq

"""
    1. 각 지점 별로 s, a, b 거리의 합을 구하고 최소가 되는 값을 리턴.
"""

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

def list_to_graph(fares):
    result = defaultdict(dict)

    for fare in fares:
        result[fare[0]][fare[1]] = fare[2]
        result[fare[1]][fare[0]] = fare[2]

    return result

def get_distance(graph, node, s, a, b):
    dist_graph = dijkstra(graph, node)
    
    return dist_graph[s] + dist_graph[a] + dist_graph[b]

def solution(n, s, a, b, fares):
    answer = 200 * 100000
    
    graph = list_to_graph(fares)
    
    for key in graph.keys():
        distance = get_distance(graph, key, s, a, b)
        answer = distance if distance < answer else answer
    
    return answer