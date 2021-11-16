from collections import defaultdict

MAX_LEN = 20

def solution(participant, completion):
    p_dict = defaultdict(list)
    c_dict = defaultdict(list)
    for p in participant:
        p_dict[len(p)].append(p)
    for c in completion:
        c_dict[len(c)].append(c)

    for l in range(1, MAX_LEN + 1):
        if len(c_dict[l]) != len(p_dict[l]):
            print(l)
            for i in c_dict[l]:
                p_dict[l].remove(i)
            return p_dict[l][0]

    return []
    