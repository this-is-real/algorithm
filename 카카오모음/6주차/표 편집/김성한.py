class Row:
    def __init__(self, prev, next):
        self.prev = prev
        self.next = next

def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    table = [Row(i-1, i+1) for i in range(n)]
    del_list = []
    
    for c in cmd:
        if c == "C":
            row = table[k]
            del_list.append((k, row.prev, row.next))
            answer[k] = "X"
            
            if row.next == n:
                k = row.prev
            else:
                k = row.next

            if row.prev == -1:
                table[row.next].prev = row.prev
            elif row.next == n:
                table[row.prev].next = row.next
            else:
                table[row.prev].next = row.next
                table[row.next].prev = row.prev
        elif c == "Z":
            i, prev, next = del_list.pop()
            answer[i] = "O"
            if prev == -1:
                table[next].prev = i
            elif next == n:
                table[prev].next = i
            else:
                table[prev].next = i
                table[next].prev = i
        else:
            direct, cnt = c.split(" ")
            if direct == "D":
                for _ in range(int(cnt)):
                    if k == n:
                        break
                    k = table[k].next
            elif direct == "U":
                for _ in range(int(cnt)):
                    if k == -1:
                        break
                    k = table[k].prev
                
    return "".join(answer)