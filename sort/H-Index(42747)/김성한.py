# 성공

def solution(citations):
    n = len(citations)
    h = n
    while True:
        a_list = [c for c in citations if c >= h]
        b_list = [c for c in citations if c not in a_list]
        if len(a_list) >= h and sum([True if b <= h else False for b in b_list]) == len(b_list):
            break
        else:
            h -= 1
    return h