# 최단 경로를 찾는 문제이므로 BFS를 사용해야 함

from collections import deque

def get_sim_list(word, target_words):
    lst = []
    for target_word in target_words:
        check = [w == t_w for w, t_w in zip(word, target_word)]
        if sum(check) == len(word)-1:
            lst.append(target_word)
    return lst

def bfs(graph, begin, target):
    queue = deque([(begin, [begin])]) # while문 안의 for문에서 queue에 append하는 시점의 visited 목록이 필요하다.
    answer = None
    while queue:
        now_word, visited = queue.popleft()
        if now_word == target:
            answer = visited
            break
        for target_word in graph[now_word]:
            if target_word not in visited:
                queue.append((target_word, visited + [target_word]))
    return len(answer) - 1
        

def solution(begin, target, words):
    if target not in words: # 변환할 수 없는 경우
        return 0
    
    graph = dict() # 인접한 단어 ({단어: 한 글자만 다른 단어 리스트})
    for word in [begin] + words:
        graph[word] = get_sim_list(word, [begin] + words)
        
    answer = bfs(graph, begin, target)
            
    return answer