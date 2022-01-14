def solution(n, k, cmd):
    answer = ''
    
    rows = [i for i in range(n)]
    del_rows = []
    
    for command in cmd:
        if command[0] == 'U':
            k = k - int(command.split(' ')[1])
        elif command[0] == 'D':
            k = k + int(command.split(' ')[1])
        elif command[0] == 'C':
            del_rows.append((rows[k], k))

            if k != len(rows)-1:
                rows = rows[:k] + rows[k+1:]
            else:
                rows = rows[:k]

            if k == len(rows):
                k = k - 1

        elif command[0] == 'Z':
            row, k_idx = del_rows.pop()
            if k >= k_idx:
                k = k + 1        

            rows = rows[:k_idx] + [row] + rows[k_idx:]

    answer = ["O"] * n
    for row, _ in del_rows:
        answer[row] = "X"

    return "".join(answer)