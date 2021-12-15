def is_proper(u):
    stack = 0
    for i in u:
        if i == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    else:
        return True

def split_uv(p):
    idx = 0
    count = 1
    while count != 0:
        if idx == 0:
            count = 0  # initialize
        if p[idx] == '(':
            count += 1
        else:
            count -= 1
        idx += 1
    return p[:idx], p[idx:]
    
def solution(p):
    answer = ''
    map_p = ['(', ')']
    if is_proper(p) or p == "":
        return p
    u, v = split_uv(p)
    if is_proper(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1]:
            answer += map_p[(map_p.index(i)+1) % 2]
        return answer
    return answer