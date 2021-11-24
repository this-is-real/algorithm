# 성공

from itertools import permutations

def is_prime(n):
    if n in [0, 1]: return False
    for i in range(2, n):
        if n % i == 0: # 나눠지면 해당 수는 소수가 아님
            return False
        if i*i > n: # i가 sqrt(n) 보다 커지면 중지 (시간 효율성)
            break
    return True

def solution(numbers):
    answer = 0
    num_lst = []
    for i in range(len(numbers)):
        for comb in permutations(list(numbers), i+1):
            num_lst.append(int(''.join(comb)))

    for num in set(num_lst):
        if is_prime(num):
            answer += 1
    return answer