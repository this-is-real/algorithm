def bal(p):
    sum = 0
    for i in p:
        if i == '(': sum += 1
        else: sum += -1
    if sum == 0 : return True
    else: return False

def collect(p):
    sum = 0
    if bal(p) == False: return False
    for i in p:
        if i == '(': sum += 1
        else: sum += -1
        if sum < 0 : return False
    return True

def solution(p):
    answer = ''
    u = ''
    v = ''
    if len(p) == 0 : return ""
    
    if collect(p): return p
    
    for i in range(2, len(p)+1, 2):
        if bal(p[:i]):
            u = p[:i]
            v = p[i:]
            break
    if collect(u): return u + solution(v)
    else: 
        result = '(' + solution(v) + ')'
        for r in u[1:-1]:
            if r == '(' : result += ')'
            else: result += '('
        return result
