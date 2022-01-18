import re
from itertools import product
def solution(user_id, banned_id):
    re_banned = []
    for item in banned_id:
        re_string = ""
        for c in item:
            if c != '*':
                re_string += c
            else :
                re_string += '[a-z0-9]'
        re_banned.append(re_string)
    total_list = []
    for item in re_banned:
        banned_list = []
        for user in user_id:
            result = re.findall(item, user)
            if result != '' and result != [] and result[0] not in banned_list and result[0] in user_id:
                banned_list.append(result[0])
        total_list.append(banned_list)
        
    product_list = list(product(*total_list))
    result = []
    for item in product_list:
        set_item = set(item)
        if set_item not in result and len(set_item) == len(banned_id):
            result.append(set_item)
    answer = len(result)
    
    return answer