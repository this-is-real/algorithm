def solution(numbers):
    answer = ''
    n = []
    
    for i in numbers:
    	n.append(str(i)*3)
    n = sorted(n, reverse = True)
    
    for i in n:
        answer += i[:len(i)//3]
        
    if int(answer) == 0:
        answer = '0'
    return answer
