def solution(record):
    from collections import defaultdict
    record_split = [record[item].split() for item in range(len(record))]   # 띄어쓰기 기준으로 잘라서 2차원 리스트 만들기
    result = []                                                            # 최종 기록 저장할 result
    IDs = defaultdict(str)                                                 # ID 변경 기록을 저장해둘 dict

    for log in record_split :                                              # 잘린 기록들을 하나씩 돌면서
        if log[0] == 'Enter' or log[0] == 'Change':                        # Enter나 Change로 닉네임을 바꿀 수 있으므로
            IDs[log[1]] = log[2]                                           # 바꿔준다.

    for log in record_split :                                              # 기록을 뽑기 위한 for문
        if log[0] == 'Enter' :                                             # 사용자가 들어오면
            result.append(f'{IDs[log[1]]}님이 들어왔습니다.')               # ID 정보를 찾아서 바뀐 닉네임으로 모두 추가
        elif log[0] == 'Leave' :                                           # 사용자가 나갈 때도 마찬가지로 처리
            result.append(f'{IDs[log[1]]}님이 나갔습니다.')    
                         
    return result