def solution(record):
    answer = []
    user = {}
    for r in record:# 유저 아이디로 구분
        r_split = r.split(' ')
        if r_split[0] == 'Enter' or r_split[0] == 'Change':
            user[r_split[1]] = r_split[2]
    for r in record:
        r_split = r.split(' ')
        if r_split[0] == 'Enter':
            answer += [user[r_split[1]]+"님이 들어왔습니다."]
        elif r_split[0] == 'Leave':
            answer += [user[r_split[1]]+"님이 나갔습니다."]
    return answer
