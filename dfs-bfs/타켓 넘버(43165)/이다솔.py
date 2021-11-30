from itertools import product
def solution(numbers, target):
    nums_minus = [-n for n in numbers]
    numbers.extend(nums_minus)
    product_nums = list(product(numbers, repeat=5))
    answer = 0 
    for nums in product_nums :
        if sum(nums) == target :
            answer += 1
    return answer
