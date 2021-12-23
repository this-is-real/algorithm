import re
from itertools import permutations

def get_operation_list(lst):
    operators = set([l for l in lst if l in ['*', '+', '-']])
    operation_list = []
    for operation in permutations(operators):
        operation_list.append(list(operation))
    return operation_list

def calc(a, b, operator):
    a, b = int(a), int(b)
    if operator == "*":
        return a*b
    elif operator == "+":
        return a+b
    elif operator == "-":
        return a-b

def get_calc_result(lst, operations):
    for operation in operations:
        while operation in lst:
            i = lst.index(operation)
            lst = lst[:i-1] + [calc(lst[i-1], lst[i+1], lst[i])] + lst[i+2:]
    return abs(lst[0])

def solution(expression):
    answer = 0
    lst = re.findall(r"\d+|[*+-]{1}", expression)
    operations_list = get_operation_list(lst)
    for operations in operations_list:
        result = get_calc_result(lst, operations)
        answer = max(answer, result)
    
    return answer