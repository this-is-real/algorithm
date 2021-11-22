def solution(priorities, location):
    nums = []
    for idx in range(len(priorities)) :
        nums.append((idx, priorities[idx]))
    printed = []
    while priorities :
        for paper in nums :
            if paper[1] != max(priorities) :
                nums.append(nums.pop(0))
                break
            else :
                printed.append(paper)
                nums.remove(paper)
                priorities.remove(paper[1])
                break
    for item in printed :
        if item[0] == location :
            answer = printed.index(item) + 1
    return answer