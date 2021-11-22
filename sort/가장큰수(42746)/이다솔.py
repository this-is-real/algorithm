# 시간 초과
# def solution(numbers):
#     from itertools import permutations
#     numbers = list(map(str, numbers))
#     num_all = list(permutations(numbers))
#     answer = [''.join(list(item)) for item in num_all]
#     return max(answer)

def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key = lambda x : x * 3, reverse=True)
    return str(int(''.join(nums)))