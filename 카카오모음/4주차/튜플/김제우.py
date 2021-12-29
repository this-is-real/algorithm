def solution(s):
    s = s.split('}')
    new_s = []
    for item in s :
        if item:
            temp = [i for i in item.replace('{','').split(',') if i]
            new_s.append(temp)
    sorted_s = sorted(new_s,key=lambda x : len(x))
    result = []
    for s in sorted_s:
        for i in s:
            if int(i) not in result:
                result.append(int(i))       
        
    answer = result
    return answer