def solution(record):
    logs = [log.split() for log in record]
    uid_to_nick = { logs[i][1]:logs[i][2] for i in range(len(logs)) if logs[i][0] == 'Enter' or logs[i][0] =='Change' }
    result = []
    for i, _ in enumerate(logs):
        command = logs[i][0]
        uid = logs[i][1]
        if command == "Enter":
            result.append(f'{uid_to_nick[uid]}님이 들어왔습니다.')
        elif command == "Leave":
            result.append(f'{uid_to_nick[uid]}님이 나갔습니다.')
            
    answer = result
    
    return answer