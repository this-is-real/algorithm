def solution(clothes):
    answer = 1
    category = list(set([clothes[i][1] for i in range(len(clothes))]))
    only_clothes = [[] for i in range(len(category))]
    for item in clothes :
        only_clothes[category.index(item[1])].append(item[0])
    for item in only_clothes :
        answer *= len(item) + 1
    return answer - 1