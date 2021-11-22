'''
풀이 못함. (다시 풀어서 업로드 예정)
'''

def solution(progresses, speeds):
    answer = []
    count = 1
    day = 0
    flag = False
    progress = None
    speed = None
    while progresses :
        if progress == None and speed == None:
            progress = progresses.pop(0)
            speed = speeds.pop(0)
        day = ((100-progress)//speed)+1
        while progresses:
            progress = progresses.pop(0)
            speed = speeds.pop(0)
            count += 1
            if day*speed + progress < 100:
                break
        answer.append(count)
        count = 1
        # if day*speed + progress >= 100:
        #     count += 1
        # else :
        #     flag = True
        #     day = ((100-progress)//speed)+1
        # if flag :
        #     answer.append(count)
        #     count = 1
        #     flag = False
            
        
    
    # while progresses:
    #     progress = progresses.pop(0)
    #     speed = speeds.pop(0)
    #     print(progress, speed)
    #     if progress + speed >= 100:
    #         count += 1
    #     else :
    #         if count != 0 :
    #             answer.append(count)
    #         progresses.append(progress)
    #         speeds.append(speed)
    #         count = 0
    # print(answer)
            
        
    # while progresses != []:
    #     for i,progress in enumerate(progresses):
    #         progresses[i] = progress+speeds[i]
    #     count = 0
    #     while progresses[0] >= 100 :
    #         progresses.pop(0)
    #         speeds.pop(0)
    #         count += 1
    #     if count != 0:
    #         answer.append(count)
    #     print(answer)
        
    return answer