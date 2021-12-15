def is_valid_str(s):
    stack = []
    for ss in s:
        if ss == "(":
            stack.append(ss)
        elif ss == ")":
            if not stack:
                return False
            stack.pop()
    return True
            
def split_str(s):
    cnt = 0
    for i in range(len(s)):
        cnt += 1 if s[i] == "(" else -1
        if cnt == 0:
            return s[:i+1], s[i+1:]

def solution(p):
    if not p:
        return ""
    
    u, v = split_str(p)
    
    if is_valid_str(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + "".join(["(" if uu == ")" else ")" for uu in u[1:-1]])