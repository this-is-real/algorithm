from collections import Counter
import math
def make_set(string):
    result = []
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1,len(string)):
        splited_f = string[i-1]
        splited_b = string[i]
        if splited_f in alphabets and splited_b in alphabets :
            result.append(f"{splited_f}{splited_b}")
    return result
    
def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = make_set(str1)
    str2_set = make_set(str2)
    # 합집합
    sum_set = str1_set + str2_set
    count_sum_set = Counter(sum_set)
    # 교집합
    # 같은 원소 찾기
    str1_str2 = Counter(str1_set) - Counter(str2_set)
    str2_str1 = Counter(str2_set) - Counter(str1_set)
    same_set = Counter(sum_set) - str1_str2 - str2_str1
    
    sum_count = 0
    for item in count_sum_set:
        sum_count += count_sum_set[item]
    
    same_count = 0
    for item in same_set:
        same_count += same_set[item]
    same_count = same_count // 2
    
    
    sum_count = sum_count - same_count
    if sum_count != 0:
        result = 65536 * same_count/sum_count
    else :
        result = 65536
    result = math.trunc(result) 
    answer = result
    return answer