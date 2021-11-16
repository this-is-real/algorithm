def solution(clothes):
    check = {}
    sum = 1
    for i in clothes:
        check[i[1]] = 1

    for i in clothes:
        check[i[1]] += 1

    for i in check :
        sum = sum * check[i]
    return sum - 1
