def solution(s):
    answer = []
    tokens=[]

    tmp = s[2:-2] # 숫자만 인덱싱
    tmp = tmp.split("},{") 
    print(tmp)
    
    for t in tmp:
        temp = list(map(int,t.split(","))) # 숫자 별로 나누기
        tokens.append(temp)
    tokens = sorted(tokens, key = lambda x: len(x))
    for token in tokens:
        for num in token:
            if num not in answer:                
                answer.append(num)
    return answer
