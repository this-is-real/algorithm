def distance(x,y):
    return sum([abs(i-j) for i,j in zip(x,y)])

def solution(numbers, hand):
    answer = ''
    num_coords = list(zip([1,0,1,2,0,1,2,0,1,2], [0,3,3,3,2,2,2,1,1,1]))
    pos_l, pos_r = (0,0),(2,0)
    for input in numbers:
        if input in [1,4,7]:
            answer += 'L'
            pos_l = num_coords[input]
            
        elif input in [3,6,9]:
            answer  += 'R'
            pos_r = num_coords[input]
            
        else:
            if distance(num_coords[input], pos_l) < distance(num_coords[input], pos_r):
                answer += 'L'
                pos_l = num_coords[input]
            
            elif distance(num_coords[input], pos_l) > distance(num_coords[input], pos_r):
                answer += 'R'
                pos_r = num_coords[input]
                
            else:
                answer += str(hand[0].upper())
                if hand[0] == 'l': pos_l = num_coords[input]
                else: pos_r = num_coords[input]

    return answer