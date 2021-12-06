def equal_check(begin, word):
    count = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            count += 1
    if count == 1:
        return True
    return False

def bfs(graph, start, destination):
    visited = []
    count = 0
    queue = [(start,[start])]
    while queue:
        node, path = queue.pop(0)
        if node == destination:
            return len(path) -1
        else:
            for m in set(graph[node]) - set(path):
                queue.append((m,path+[m]))
    return 0

def solution(begin, target, words):
    #그래프 만들기
    if target not in words:
        return 0
    words.insert(0,begin)
    graph = {}
    for word1 in words:
        for word2 in words:
            if word1 not in graph:
                if equal_check(word1,word2):
                    graph[word1] = [word2]
            else :
                if equal_check(word1,word2):
                    graph[word1].append(word2)
    
    answer = bfs(graph,begin, target)
    
    
    return answer