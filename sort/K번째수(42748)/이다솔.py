def solution(array, commands):
    answer = []
    for com in commands :
        i, j, k = com[0] - 1, com[1], com[2] - 1
        answer.append(sorted(array[i : j])[k])
    return answer