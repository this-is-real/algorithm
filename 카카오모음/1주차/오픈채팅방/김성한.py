def solution(record):
    answer = []
    status = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    users = dict()
    
    for r in record:
        info = r.split(" ")
        if info[0] == "Enter":
            users[info[1]] = info[2]
            answer.append((info[1], info[0]))
        elif info[0] == "Leave":
            answer.append((info[1], info[0]))
        elif info[0] == "Change":
            users[info[1]] = info[2]
    
    answer = [users[ans[0]] + "님이 " + status[ans[1]] for ans in answer]
    
    return answer