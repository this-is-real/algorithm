def solution(array, commands):
    answer = []
    c = []
    for i in range(len(commands)):
        c = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(c[commands[i][2]-1])
    return answer
