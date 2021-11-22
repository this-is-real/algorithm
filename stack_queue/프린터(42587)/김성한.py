# 성공

def solution(priorities, location):
    lst = [(p, i) for i, p in enumerate(priorities)]
    printed = []
    while True:
        if len(lst) == 1:
            printed.extend(lst)
            break
        doc = lst.pop(0)
        if doc[0] >= max([l[0] for l in lst]):
            printed.append(doc)
        else:
            lst.append(doc)
    answer = [i+1 for i, (_, j) in enumerate(printed) if j == location][0]
    return answer