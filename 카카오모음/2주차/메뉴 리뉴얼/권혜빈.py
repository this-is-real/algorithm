from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            conb = combinations(sorted(order), c)
            temp += conb
        counter = Counter(temp)
        if counter:
            max_ = max(list(counter.values()))
            if max_ >= 2:
                for k, v in counter.items():
                    if v == max_:
                        answer.append(''.join(k))
    return sorted(answer)
