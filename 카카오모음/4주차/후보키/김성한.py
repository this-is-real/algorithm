from itertools import combinations

def get_candidates(num):
    result = []
    num_list = [i for i in range(num)]
    for i in range(1, num+1):
        for comb in combinations(num_list, i):
            result.append(list(comb))
    return result

def get_value_list(candidate, relation):
    result = []
    for i in range(len(relation)):
        values = []
        for j in candidate:
            values.append(relation[i][j])
        result.append("".join(values))
    return result
        

def check_unique(lst):
    return len(lst) == len(set(lst))

def check_already_include(candidate, result):
    check_include = False
    for i in range(1, len(candidate)):
        if not check_include:
            for comb in combinations(candidate, i):
                if list(comb) in result:
                    check_include = True
                    break
    return check_include

def solution(relation):
    result = []
    candidates = get_candidates(len(relation[0]))
    for candidate in candidates:
        value_list = get_value_list(candidate, relation)
        if check_unique(value_list):
            if not check_already_include(candidate, result):
                result.append(candidate)
    return len(result)