import collections
import re

def solution(s):
    c = collections.Counter(re.sub(r'[{}]', '', s).split(','))
    return [int(k) for k,_ in c.most_common()]