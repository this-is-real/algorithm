def solution(citations):
    citations  = sorted(citations)
    for i in range(len(citations),0,-1):
        if sum([val >= i for val in citations[-i:]]) == i:
            return i
    return 0
