def solution(s):
    windows = [i for i in range(1,len(s)//2 + 1)]
    result = []
    if len(s) == 1:
        return 1
    for win_size in windows:
        s_poped = s[0:win_size]
        s_remain = s[win_size:]
        s_stack = ""
        count = 1
        for i in range(len(s)//win_size):
            if s_poped == s_remain[0:win_size]:
                count += 1
            else :
                if count == 1:
                    s_stack += s_poped
                else :
                    s_stack += str(count)+s_poped
                count = 1
            s_poped = s_remain[0:win_size]
            s_remain = s_remain[win_size:]
        if count == 1:
            s_stack += s_poped
        else :
            s_stack += str(count)+s_poped
        result.append(len(s_stack))
    answer = min(result)
    return answer