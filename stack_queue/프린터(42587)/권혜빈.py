def solution(prior, location):
    loc = list(range(len(prior)))
    print(loc)
    p_l = list(zip(prior,loc))
    count = 0
    while p_l: 
        for i in range(1,len(p_l)):
            if p_l[0][0]<p_l[i][0]: 
                p_l.append(p_l[0])
                del p_l[0]
                break
        if max(p_l)[0] == p_l[0][0]:
            count += 1
            if p_l[0][1] == location:
                return count
            else :
                del p_l[0]
