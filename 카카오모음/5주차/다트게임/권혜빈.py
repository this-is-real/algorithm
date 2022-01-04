def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'Z')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for i in dartResult:
        if i == 'Z' :
            answer.append(10)
        elif i in ['S', 'D', 'T'] :
            answer[-1] = answer[-1] ** bonus[i]
        elif i == '#' :
            answer[-1] *= -1
        elif i == '*' :
            answer[-1] *= 2
            if len(answer) > 1 :
                answer[-2] *= 2
        else :
            answer.append(int(i))
    return sum(answer)
