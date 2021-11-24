from itertools import permutations

def find(n):
    if int(n) <= 1: 
        return False
    for i in range(2, int(n)//2+1):
        if int(n)%i == 0:
            return False
    return True

def solution(numbers): # 002
    answer = 0
    total = []
    for i in range(1, len(numbers)+1):
        tmp = permutations(numbers, i)
        
        for j in tmp:
            total.append(int(''.join(j)))

    total = list(set(total))
    answer = len(total)
    
    for i in total:
        if i<=1:
            answer -= 1
        else:
            if find(i):
                continue
            else:
                answer -= 1
                
    return answer
