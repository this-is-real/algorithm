from itertools import permutations
from math import floor, sqrt

def solution(numbers):
    samp = []
    
    for i in range(1, len(numbers)+1):   
        samp += [int("".join(p)) for p in permutations(numbers, i)]
    
    se = set(samp) - set(range(2))
    answer = len(se)
    
    for i in list(se):
        for j in range(2, floor(sqrt(i))+1):
            if i % j == 0:
                answer -= 1
                break
    return answer