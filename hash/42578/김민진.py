from collections import Counter

def solution(clothes):
    answer = 1
    _, types = zip(*clothes)
    counter = Counter(types)
    for count in counter.values():
        answer *= (count + 1)
    return answer - 1
    