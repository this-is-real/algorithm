def solution(record):
    answer = []
    id2name = {}
    for input in record:
        act_name = input.split(' ')

        if act_name[0] == 'Enter':
            answer.append([act_name[1],"님이 들어왔습니다."])
            id2name[act_name[1]] = act_name[2]
        elif act_name[0] == 'Leave':
            answer.append([act_name[1],"님이 나갔습니다."])
        else:
            id2name[act_name[1]] = act_name[2]

    return [id2name[id]+act for id,act in answer]