def solution(citations):
    answer = 0
    h_dict={}
    count = 0
    for i in range(len(citations)+1):
        for number in citations:
            if number >= i :
                count += 1
        h_dict[i] = count
        count = 0
    for i in range(len(citations)+1):
        if h_dict[i] >= i:
            result = i
    answer = result
    return answer