import collections
def solution(participant, completion):
    par = collections.Counter(participant)
    com = collections.Counter(completion)
    answer = par - com
    return list(answer.keys())[0]