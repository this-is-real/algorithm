from itertools import combinations
def check_inner_2(x1,x2, y1,y2):
    dist = abs(x1-y1) + abs(x2-y2)
    if dist <= 2:
        return True
    else :
        return False
    
def check_inner_1(x1,x2, y1,y2):
    dist = abs(x1-y1) + abs(x2-y2)
    if dist <= 1:
        return True
    else :
        return False
def solution(places):
    answer = []
    
    for place in places:
        # P들의 좌표 구하기
        result = 1
        p = []
        for i, row in enumerate(place):
            for j,item in enumerate(row) :   
                if item == "P":
                    p.append((i,j))
        
        in2p = []
        for item in combinations(p,2):
            if check_inner_2(item[0][0],item[0][1],item[1][0],item[1][1]) :
                in2p.append(item)
                
        for item in in2p:
            x1 = item[0][0]
            y1 = item[0][1]
            x2 = item[1][0]
            y2 = item[1][1]
            #거리 1체크
            if check_inner_1(x1,y1,x2,y2):
                result = 0
                break
            #직선 체크 세로
            elif x1 == x2:
                if place[x1][(y1 + y2) // 2] != 'X':
                    result = 0
                    break
            #직선 체크 가로
            elif y1 == y2:
                if place[(x1 + x2) // 2][y1] != 'X':
                    result = 0
                    break
            #대각선 체크
            else :
                if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                    result = 0
                    break
        answer.append(result)
                    
        # 대각선일때는 위아래 전부
    return answer