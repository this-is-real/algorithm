def solution(numbers, target):
    total = [0]
    for i in numbers:
        tmp = []
        for j in total : 
            tmp.append(j+i)
            tmp.append(j-i)
        total = tmp
    return total.count(target)
