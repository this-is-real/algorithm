def solution(brown, yellow) :
    cases = [(num, yellow // num) for num in range(yellow, 0, -1) if yellow % num == 0] # yellow부터 약수를 구하는 이유: 가로 길이 >= 세로 길이
    for item in cases :                                                                 
        if brown + yellow == (item[0] + 2) * (item[1] + 2) : # 전체 격자의 수 == (yellow 가로 + 2) * (yello 세로 + 2)
            return [item[0] + 2, item[1] + 2]
            # break    ->     난 break를 해야 더 빠를 줄 알았는데 비교해보니 break 있는 게 더 느려짐
            
            
x = [1, 6,4, 754, 7,3, 23, 41, 10]
print(list(set(x)))