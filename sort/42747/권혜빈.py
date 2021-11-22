def solution(citations):
    count = 0
    citations = sorted(citations, reverse = True) #  [6,5,3,1,0]

    for i in range(citations[0]//2,-1,-1):
        count = 0
        for j in citations:
            if j>=i:
                count += 1
        if count >= i:
            return i
