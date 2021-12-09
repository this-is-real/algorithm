def solution(s):
    answer = len(s) # 최대길이
    if len(s) == 1: # 길이가 1일 때
        return 1
    for i in range(1, len(s)//2+1): # 자르는 범위
        count = 1 # 얼마나 반복되는지
        check = s[:i] # i만큼 자른 문자열 #a
        result = '' # 결과 저장
        for j in range(i, len(s), i): # i만큼 잘라서 검사
            if check == s[j:j+i]:
                count += 1
            else: # 문자반복이 끝났다면
                if count == 1:
                    result += check # 압축 결과 
                else :
                    result += (str(count)+check) # 압축 결과 
                    count = 1
                check = s[j:j+i]
        if count == 1: # 두번째 for문 다 돌고 나서 나온 result 처리
            result += check
        else:
            result += (str(count)+check)
        if answer > len(result):
            answer = len(result)
    return answer
