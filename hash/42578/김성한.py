# 성공

from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter([val for key, val in clothes])
    for cnt in counter.values():
        answer *= (cnt+1)
    answer -= 1
    return answer