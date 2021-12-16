def balanced(s):
    return s.count(')') == s.count('(')

def correct(s):
    stack = [0]
    for cand in s:
        if stack[-1] == '(' and cand == ')':
            stack.pop()
        else:
            stack.append(cand)
    return stack == [0]

def split(s):
    u,v = '',''
    pointer = 2
    while True:
        u = s[:pointer]
        v = s[pointer:]
        if balanced(u) and balanced(v):
            return u,v
        else:
            pointer += 2
            
def solution(p):
    if not p:
        return p
    u,v = split(p)

    if correct(u):
        return u+solution(v)
    else:
        temp = '('+solution(v)+')'
        temp += ''.join(['(' if i == ')' else ')' for i in  u[1:-1]])
        return temp