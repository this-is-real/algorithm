def is_ok(answer):
    for x, y, block_type in answer:
        if block_type: # 기둥
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
        else: # 보
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, block_type, action in build_frame:
        ans = [x, y, block_type]
        if action: # 설치
            answer.append(ans)
            if not is_ok(answer):
                answer.remove(ans)
        else: # 삭제
            answer.remove(ans)
            if not is_ok(answer):
                answer.append(ans)
    answer.sort()
    return answer