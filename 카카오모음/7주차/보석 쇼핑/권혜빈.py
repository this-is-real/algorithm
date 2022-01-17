def solution(gems):
    answer = [1, len(gems)]
    count = len(set(gems))
    gem_dict = {}
    for i in range(len(gems)):
        if gems[i] in gem_dict:
            del gem_dict[gems[i]]
        gem_dict[gems[i]] = i # 위치 저장
        if len(gem_dict) == count:
            min = list(gem_dict.values())[0]
            if i - min < answer[1] - answer[0]:
                answer = [min+1, i+1]
    return answer
    
