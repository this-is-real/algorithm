from itertools import product

def solution(numbers, target):
    new_numbers = [ [number, -number]for number in numbers]
    product_list = list(product(*new_numbers))
    count = 0
    for numbers in product_list:
        if sum(numbers) == target :
            count += 1
    answer = count
            
    return answer