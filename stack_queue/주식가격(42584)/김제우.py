def solution(prices):
    # 효율성 통과 실패 prices 인덱스 슬라이싱으로 인한 o(n)추가
    # answer = []
    # count = 0 
    # for i,price in enumerate(prices):
    #     if i != len(prices):
    #         for next_price in prices[i+1:]:
    #             count += 1
    #             if price > next_price : 
    #                 break
    #         answer.append(count)
    #         count = 0
    
    #성한님 코드 봤음
    answer = []
    n = len(prices)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
        count = 0
    
    return answer