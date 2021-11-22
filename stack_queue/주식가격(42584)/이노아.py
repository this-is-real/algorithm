from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while True:
        ind = prices.popleft()
        cnt = 0
        
        for p in prices:
            cnt+= 1
            if p < ind:              
                break
        answer.append(cnt)
                
        if len(prices) == 0:
            break
            
    return answer
