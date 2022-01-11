from math import gcd

def solution(w,h):
    answer = w * h

    gcd_num = gcd(w, h)

    w = w / gcd_num
    h = h / gcd_num

    answer = answer - ((w + h - 1) * gcd_num)
    # answer = w * h - (w + h - gcd(w, h))
    return answer