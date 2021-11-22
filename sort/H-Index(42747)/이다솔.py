def solution(citations):
    h_index = []
    for i in range(max(citations) + 1) :
        h = sum(1 if i <= other_item else 0 for other_item in citations)
        h_index.append(h)
    for j in range(len(h_index)) :
        if j > h_index[j] :
            answer = j - 1
            break
    else :
        answer = len(h_index) - 1
    return answer