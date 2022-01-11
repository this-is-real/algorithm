# def gcd(a, b):
#     return b if a % b == 0 else gcd(b, a % b)


# def solution(w, h):
#     whole = w * h
#     broken = w + h - gcd(w, h)
#     return whole - broken

import math
def solution(w,h):

    if w == 1 or h ==1 :
        return 0
    bigger = 0
    result = []
    if w > h :
        bigger = w
        for i in range(bigger):
            y = h/w*i
            f_y = math.floor(y)
            if f_y == y :
                continue
            else :
                result.append((i, f_y))
                result.append((i-1, f_y))
    elif w < h:
        bigger = h
        for i in range(bigger):
            y = w/h*i
            f_y = math.floor(y)
            if f_y == y :
                continue
            else :
                result.append((f_y,i ))
                result.append((f_y,i-1,))
    else :
        return w    
    count = len(set(result))
    answer = w*h - count
    return answer