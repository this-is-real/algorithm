def dfs(nums, i, n, t):
    answer = 0
    if i==len(nums):
        if n==t: 
            return 1
        else: 
            return 0
    answer += dfs(nums, i+1, n+nums[i], t)
    answer += dfs(nums, i+1, n-nums[i], t)
    return answer

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer