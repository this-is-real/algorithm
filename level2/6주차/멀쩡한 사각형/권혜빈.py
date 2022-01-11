import math
def solution(w,h):
    answer = 1
    if w==h: return w*h-w
    else: return w*h-(w+h-math.gcd(w,h))
