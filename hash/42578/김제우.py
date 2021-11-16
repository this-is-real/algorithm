def solution(clothes):

    clothes_dict= {}
    for name, part in clothes:
        if part not in clothes_dict:
            clothes_dict[part] = [None]
        clothes_dict[part].append(name)
    
    cross_count = 1
    for v in clothes_dict.values():
        cross_count *= len(v)
    answer = cross_count - 1

    return answer