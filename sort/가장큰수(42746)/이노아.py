def solution(numbers):
    nums = [str(i) for i in numbers]
    
    if sum(numbers) == 0:
        return '0'
    
    answer = sorted(nums, key = lambda t: t*3, reverse = True)

    return ''.join(answer)
