from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    diff = p-c
    # print(diff)
    return list(diff.keys())[0]
