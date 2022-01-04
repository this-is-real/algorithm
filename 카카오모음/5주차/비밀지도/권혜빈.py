def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s_1 = str(bin(arr1[i]))[2:]
        s_2 = str(bin(arr2[i]))[2:]
        s_1 = '0'*(n-len(s_1))+s_1      
        s_2 = '0'*(n-len(s_2))+s_2
        tmp = ''
        for j in range(n):
            if s_1[j] == '1' or s_2[j] == '1':
                tmp += '#'
            elif s_1[j] == '0' and s_2[j] == '0':
                tmp += ' '
            
        answer.append(tmp)
    
    return answer
