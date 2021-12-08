import re

def solution(s):
    dict = ['zero','one','two','three','four','five',
            'six','seven','eight', 'nine']
    if s.isdigit():
        return int(s)
    else:
        for i,num in enumerate(dict):
            s = re.sub(num,str(i),s)
        return int(s)