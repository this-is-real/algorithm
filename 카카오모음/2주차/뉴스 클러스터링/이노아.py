from collections import Counter

def preprocess(s):
    s = s.lower()
    return Counter(s[ind:ind+2] for ind in range(0,len(s)-1) if s[ind:ind+2].isalpha())

def solution(s, s1):
    c,c1 = [preprocess(string) for string in [s,s1]]
    if c == c1: return 65536    
    cnt1 = sum((c&c1).values())
    cnt2 = sum((c+c1).values())
    return int(cnt1/(cnt2-cnt1)*65536)
                   