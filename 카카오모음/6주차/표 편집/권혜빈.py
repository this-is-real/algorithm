def solution(n, k, cmd): # 행개수, 처음 행위치, 명령어들
    answer = ['O']*n # 처음엔 다 O
    graph = [i for i in range(n)] # 현재 표
    index = k # 현재 index
    del_list = [] # [당시 index, 행번호]
    for c in cmd:
        if 'D' in c: 
            index += int(c[1:])
            if index >= len(graph) : 
                index = len(graph) - 1
        elif 'U' in c: 
            index -= int(c[1:])
            if index < 0: 
                index = 0
        elif c == 'C':
            del_list.append([graph.index(graph[index]), graph[index]])
            graph.remove(graph[index])
            if index >= len(graph) : 
                index = len(graph) - 1
        else: # 'Z'
            index = graph[index]
            graph.insert(del_list[-1][0],del_list[-1][1])
            del_list = del_list[:-1]
            index = graph.index(index)
    for i in del_list:
        answer[i[1]] = 'X'
    return ''.join(answer)
