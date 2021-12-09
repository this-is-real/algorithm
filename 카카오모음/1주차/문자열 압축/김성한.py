def solution(s):
    n = len(s)
    
    if n == 1:
        return 1

    answer = 1000
    for i in range(1, n//2+1):
        splited = [s[j:j+i] for j in range(0, n, i)]
        cnt = len(splited)
        checked = [False for _ in range(cnt)]
        comp_s = ""
        for j in range(cnt):
            if checked[j]:
                continue
            checked[j] = True
            dup_cnt = 1
            for k in range(j+1, cnt):
                if splited[j] == splited[k]:
                    dup_cnt += 1
                    checked[k] = True
                else:
                    break
            comp_s = comp_s + (str(dup_cnt) if dup_cnt > 1 else "") + splited[j]
        answer = min(answer, len(comp_s))
        
    return answer