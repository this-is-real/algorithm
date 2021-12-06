from collections import defaultdict, deque

def solution(tickets):
    dict = defaultdict(list)
    # reverse 시킨 후에 dict 저장 -> pop(0) 사용 X
    for key,value in sorted(tickets,reverse = True): 
        dict[key].append(value)
        
    visited = deque()
    stack = ['ICN']
    
    # dfs
    while stack:
        temp = stack[-1]
        if temp not in dict or len(dict[temp]) == 0:
            visited.appendleft(stack.pop())     # visited에 추가
        else:
            stack.append(dict[temp].pop())      # dict pop -> stack enque
    return list(visited)