def solution(begin, target, words):
    # target 이 words에 부재 시에 0 return
    if target not in words: 
        return 0
    
    # 변환 가능 여부
    def compatible(a,b):
        return sum([i!=j for i,j in zip(a,b)])==1

    visited = [0]*len(words)
    answer = 0
    stack = [begin]
    
    # dfs
    while stack:
        temp = stack.pop()
        if temp == target:              # 변환 종료 조건
            return answer

        for idx,word in enumerate(words):
            if compatible(temp, word):  # 변환 가능 시
                if visited[idx] == 1:   # visited 된 경우 continue
                    continue
                else:
                    visited[idx] = 1     
                    stack.append(word)  # visited X -> stack enque
        answer += 1
    return answer