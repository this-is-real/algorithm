import re

def solution(s):
    answer = []
    set_list = re.findall(r"{[\d,]+}", s)
    set_list = [set_value[1:-1].split(",") for set_value in set_list]
    set_list = sorted(set_list, key=lambda x: len(x))
    for set_value in set_list:
        for value in set_value:
            if value not in answer:
                answer.append(value)
    answer = [int(ans) for ans in answer]
    return answer