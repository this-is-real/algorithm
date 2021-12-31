import pandas as pd
from itertools import combinations
def is_minimal(unique_list, item):
    result = True
    for unique in unique_list:
        if set(unique)&set(item) == set(unique):
            result = False
    return result
def solution(relation):
    col_num = len(relation[0])
    row_num = len(relation)
    cols = pd.DataFrame(relation)
    unique_list = []
    for i in range(1,len(cols.columns)+1):
        for item in list(combinations(cols.columns, i)):
            empty_list = [ "" for _ in range(row_num)]
            result = pd.Series(empty_list)
            if is_minimal(unique_list, item):
                for idx in item:
                    result += cols[idx]
                if len(result.unique()) == row_num:
                    unique_list.append(item)
    answer = len(unique_list)
    return answer