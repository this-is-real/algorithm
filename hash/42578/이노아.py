from collections import defaultdict
from math import prod

def solution(clothes):
    answer = 1
    dic = defaultdict(lambda:1) # int 로 하면 0..!
    
    for v,k in clothes:
        dic[k] += 1

# # 1번 for loop
#     for i in list(dic.values()):
#         answer *= i
        
#     return answer - 1


# 2번 math.prod() 활용
    if len(dic.values()) == 1:
        return list(dic.values())[0] - 1
    else:
        return prod(dic.values()) - 1