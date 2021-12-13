def solution(numbers, hand):
    answer = ''
    P = {1:(0, 0), 2:(0, 1), 3:(0, 2),
         4:(1, 0), 5:(1, 1), 6:(1, 2),
         7:(2, 0), 8:(2, 1), 9:(2, 2),
         '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    
    L_H = [1,4,7]
    R_H = [3,6,9]
    L = '*'
    R = '#' 
    for i in numbers:
        if i in L_H:
            L = i
            answer += 'L'
        elif i in R_H:
            R = i
            answer += 'R'
        else:
            if abs(P[L][0]-P[i][0])+abs(P[L][1]-P[i][1]) < abs(P[R][0]-P[i][0])+abs(P[R][1]-P[i][1]):
                answer += 'L'
                L = i
            elif abs(P[L][0]-P[i][0])+abs(P[L][1]-P[i][1]) == abs(P[R][0]-P[i][0])+abs(P[R][1]-P[i][1]):
                if hand == 'right':
                    answer += 'R'
                    R = i
                else:
                    answer += 'L'
                    L = i
            else:
                answer += 'R'
                R = i
            
    return answer
