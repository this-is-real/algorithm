def is_right(s):
    stack = ""
    for item in s :
        stack += item
        if stack[-2:] == '()':
            stack = stack[:-2]
    if stack == "":
        return True
    else :
        return False
    
def seperate(p):
    l_count = 0
    r_count = 0
    sep_index = len(p)+1
    for i, item in enumerate(p) :
        if item == '(':
            l_count += 1
        else :
            r_count += 1
        if l_count == r_count :
            sep_index = i
            break
    return p[:sep_index+1], p[sep_index+1:]

def recursive(w):
    if w == '':
        return ''
    u, v = seperate(w)
    if is_right(u):
        if is_right(v):
            return u+v
        else :
            v = recursive(v)
            return u+v
    else :
        result = '('
        v = recursive(v)
        result += v + ")"
        u = u[1:-1]
        new_u = ''
        for item in u :
            if item == "(":
                new_u += ")"
            else :
                new_u += "("
        result += new_u
        return result
        
def solution(p):
    answer = recursive(p)
    return answer