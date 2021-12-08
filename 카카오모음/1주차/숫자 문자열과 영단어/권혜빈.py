def solution(s):
    num = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    
    for n in range(len(num)):
        s = s.replace(num[n], str(n))
    return int(s)
