def solution(s) :
    result = []
    for split in range(1, len(s)) :                           # 1부터 s의 길이 - 1 까지 for문
        cnt, ans = 1, ''                                      # 몇 개 압축할 수 있는지 세는 cnt, 압축 결과물 ans
        word = s[0:split]                                     # 기준 단어 설정
        for i in range(split, len(s), split) :                # 기준 단어 다음부터 s의 끝까지 문자열을 나눔
            if word == s[i:i+split] :                         # 기준 단어가 그 다음 단어와 같으면 cnt + 1
                cnt += 1
            else :                                            # 같지 않으면
                ans += str(cnt) + word if cnt > 1 else word   # 압축 횟수 + 기준 단어
                word = s[i:i+split]                           # 기준 단어 재설정, cnt 초기화
                cnt = 1
        ans += str(cnt) + word if cnt > 1 else word           # for문 다 돌고나서 남아있던 단어 추가
        result.append(ans)                                    # 압축 완료된 단어 result에 추가
    result.sort(key=len)                                      # 길이 기준으로 정렬
    answer = len(result[0]) if result else len(s)             # 가장 짧은 것 반환, result가 비어있으면 그냥 문자열 길이 반환
    return answer
