# 성공

def solution(brown, yellow):
    answer = []
    y_w_list = [(i+1) for i in range(yellow//2) if yellow % (i+1) == 0] + [yellow] # 약수 구하기
    y_w_list.sort(reverse=True)
    
    for y_w in y_w_list:
        y_h = yellow // y_w
        if (y_w+2)*2 + y_h * 2 == brown: # brown 갯수로 비교
            answer = [y_w + 2, y_h + 2]
            break
    
    return answer

# 다른 풀이

def get_divisor(n):
    return [i for i in range(1, n//2+1) if n % i == 0] + [n]

def solution(brown, yellow):
    answer = [0, 0]
    for y_width in get_divisor(yellow):
        y_height = yellow // y_width
        if y_width >= y_height: # 크기로 비교
            x, y = y_width+2, y_height+2
            if x * y - yellow == brown:
                answer = [x, y]
                break
    return answer