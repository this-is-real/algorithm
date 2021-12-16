import re
from collections import Counter

def make_multi_set(s):
    return [s[i:i+2] for i in range(0, len(s)-1)]

def check(s):
    s = re.sub(r"[^a-zA-Z]+", "", s)
    return len(s) > 1

def calc_output(score):
    return int(score * 65536)

def solution(str1, str2):
    set1 = [s1.lower() for s1 in make_multi_set(str1) if check(s1)]
    set2 = [s2.lower() for s2 in make_multi_set(str2) if check(s2)]
    
    if not set1 and not set2:
        return calc_output(1)
    
    counter1, counter2 = Counter(set1), Counter(set2)
    key1, key2 = set(counter1.keys()), set(counter2.keys())
    
    intersection = key1 & key2
    union = key1 | key2
    
    i_cnt = 0
    for i in intersection:
        i_cnt += min(counter1[i], counter2[i])
        
    u_cnt = 0
    for u in union:
        u_cnt += max(counter1[u], counter2[u])
        
    return calc_output(i_cnt / u_cnt)