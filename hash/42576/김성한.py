# 성공

from collections import Counter

def solution(participant, completion):
    answer = [k for k in (Counter(participant) - Counter(completion)).keys()][0]
    return answer