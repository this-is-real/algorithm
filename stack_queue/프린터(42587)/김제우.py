def solution(priorities, location):
    answer = 0
    count = 0
    priorities = [(1,priority ) if i == location else (0,priority) for i, priority in enumerate(priorities)]
    while True:
        (flag, priority) = priorities.pop(0)

        #같은걸 가지고 있는지 탐색
        have_bigger = False
        for (_,item) in priorities:
            if priority < item :
                have_bigger = True
        if have_bigger :
            priorities.append((flag,priority))
        else :
            count += 1
            if flag == 1 :
                answer = count
                break
            
    return answer