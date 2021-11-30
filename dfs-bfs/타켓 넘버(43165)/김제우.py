# 풀이 실패

# def dfs(graph, start_node):
#     visit = list()
#     stack = list()
#     stack.append(start_node)

#     while stack:
#          node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])

#     return visit

def solution(numbers, target):
    new_numbers = [ [number, -number]for number in numbers]
    
    result = []
    stack = [0 for _ in range(len(numbers))]
    print(stack)
    for i in range(len(numbers)*2): # 0
        for number in [-1,1]:  # -1
            stack[i] = number # -1 
            result.append(stack) # [-1,0,0,0,0] , [1,0,0,0,0] , [1,-1,0,0,0], [1,1,0,0,0]
    print(result)
        
    
#     for i in range(2):
#         for number_set in new_numbers:
#             stack.append(number_set[i])
#             print(stack)
#             if sum(stack) == 3:
#                 result.append(stack)
#                 stack = []        
            
    answer = 0
    return answer