import re
def solution(expression):
    toList = re.split("(\d+)", expression)[1:-1]  # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    order = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
    answer = 0
    for i in order:
        exp = toList[:]  # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
        while i[0] in exp:
            idx = exp.index(i[0])
            exp[idx-1] = str(eval(exp[idx-1] + exp.pop(idx) + exp.pop(idx)))
        while i[1] in exp:
            idx = exp.index(i[1])
            exp[idx-1] = str(eval(exp[idx-1] + exp.pop(idx) + exp.pop(idx)))
        while i[2] in exp:
            idx = exp.index(i[2])
            exp[idx-1] = str(eval(exp[idx-1] + exp.pop(idx) + exp.pop(idx)))
        if abs(int(exp[0])) > answer:
            answer = abs(int(exp[0]))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))