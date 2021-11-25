def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, total//3+1):
        if total%i == 0 and 2*(i+total//i-2) == brown:
            return [total//i, i]
