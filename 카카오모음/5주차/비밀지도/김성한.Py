def convert_to_map(n, arr):
    return [bin(a)[2:].rjust(n, '0') for a in arr]

def solution(n, arr1, arr2):
    answer = [[' ' for _ in range(n)] for _ in range(n)]
    map1 = convert_to_map(n, arr1)
    map2 = convert_to_map(n, arr2)
    
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                answer[i][j] = '#'
    
    answer = [''.join(ans) for ans in answer]
    return answer