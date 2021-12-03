def solution(n, computers):
    computer_list = [i for i in range(len(computers))]
    graph = {}
    # 단방향 처리
    for i,computer in enumerate(computers):
        for j,item in enumerate(computer):
            if item == 1:
                computers[j][i] = 1
    # graph 생성
    for i, computer in enumerate(computers):
        graph[i] = [j for j, connect in enumerate(computer) if connect == 1 and j != i]
    
    # 자기 자신만 가지고 있는 loop 제거
    count = 0
    delete_list=[]
    for item in graph:
        if graph[item] == []:
            count += 1
            delete_list.append(item)
    for delete in delete_list :
        del graph[delete]
        computer_list.remove(delete)
    
    # dfs를 이용한 graph 생성
    graph_list=[]
    while computer_list:
        visited = [computer_list[0]]
        stack = [computer_list[0]]
        for i in graph:
            progress = stack.pop()
            stack.extend(graph[progress])
            for node in stack:
                if node not in visited :
                    visited.append(node)
        graph_list.append(visited)
        for node in visited:
            computer_list.remove(node)
    count += len(graph_list)
    answer = count
    return answer



