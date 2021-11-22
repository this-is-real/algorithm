'''
풀이 못함. (다시 풀어서 업로드 예정)
'''

def solution(citations):
    h_list = []
    
    for number in sorted(citations):
        count = 0
        for citation in citations:
            if citation >= number :
                count += 1
        if count >= number:
            h_list.append(number)
    if h_list :
        answer = max(h_list)
    else :
        answer = 1
    return answer