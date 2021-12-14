from itertools import combinations
from collections import Counter
def solution(orders, course):
    comb_list = []
    for length in course:
        for order in orders:
            comb_list.append([''.join(sorted(item)) for item in combinations(order, length)])
            
    result = Counter()
    for i in range(0,len(comb_list)):
        result += Counter(comb_list[i])
        
    answer = []
    for i,item in enumerate(result.most_common()) :
        if i == 0 and item[1] != 1:
            answer.append(item[0])
            leng = len(item[0])
            cur_num = item[1]
            continue
        if leng < len(item[0]) and item[1] != 1:
            answer.append(item[0])
            cur_num = item[1]
            leng = len(item[0])
        elif cur_num == item[1]:
            answer.append(item[0])
    answer = sorted(answer)
    return answer
    
# from itertools import permutations
# def solution(orders, course):
#     order_set = {}
#     for length in course:
#         permutes_list = [list(permutations(order, length)) for order in orders]
        
#         for permutes in permutes_list:
#             for permute in permutes:
#                 key = permute[0]+str(length)
#                 value = ""
#                 for item in permute[1:]:
#                     value +=item
#                 if key not in order_set :
#                     order_set[key] = [[1,value]]
#                 else :
#                     exist = False
#                     for item in order_set[key]:
#                         if item[1] == value:
#                             item[0]+= 1
#                             exist = True
#                     if exist == False :
#                         order_set[key].append([1,value])
#     result = []
#     for key in order_set:
#         for item in order_set[key]:
#             result.append((item[0],key[0]+item[1]))

#     best = {}
#     for item in result:
#         sets = item[1]
#         count = item[0]
#         if count != 1:
#             if len(sets) not in best :
#                 best[len(sets)] = [item]
#             else :
#                 if best[len(sets)][0][0] < count :
#                     best[len(sets)] = [item]
#                 elif best[len(sets)][0][0] == count :
#                     best[len(sets)].append(item)
#     answer = []
#     for values in best.values() :
#         for item in values:   
#             order = ''.join(sorted(item[1]))
#             if order not in answer:
#                 answer.append(order)
#     answer = sorted(answer)
#     return answer