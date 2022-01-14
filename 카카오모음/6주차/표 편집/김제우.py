#실패
def solution(n, k, cmds):
    remove_list = []
    stack = [0 for _ in range(n)]
    now = k
    p = 0
    for cmd in cmds:
        if len(cmd) == 1:
            if cmd == "C":
                stack.pop(now)
                if remove_list == [] :
                    remove_list.append(now)
                    p = now
                    if now == len(stack) :
                        now = len(stack)-1
                    else :
                        now = now
                else :
                    p_real = remove_list[-1]
                    remove_list.append(now-p+1+p_real)
                    p = now
            elif cmd == "Z" :
                remove_list.pop()
                stack.insert(p,0)
        elif len(cmd) == 3:
            cmd_split = cmd.split()
            if cmd_split[0] == 'D':
                now += int(cmd_split[1])
            elif cmd_split[0] == 'U':
                now -= int(cmd_split[1])
    # print(remove_list)
    result = ["O" for _ in range(n)]
    for item in sorted(remove_list):
        result[item] = 'X'
    # print(result)
    answer = "".join(result)
    return answer