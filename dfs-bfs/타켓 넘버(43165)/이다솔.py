def solution(numbers, target):
    from itertools import product
    nums_all = [(n, -n) for n in numbers]
    product_nums = list(product(*nums_all))
    answer = 0
    for nums in product_nums :
        if sum(nums) == target :
            answer += 1
    return answer
