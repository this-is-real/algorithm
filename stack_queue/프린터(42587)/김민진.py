from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([*enumerate(priorities)])
    sort_p = deque(sorted(priorities, reverse=True))  # 내림차순
    while q:
        head = q[0]
        if head[1] == sort_p[0]:
            answer += 1
            if head[0] == location:
                return answer
            q.popleft()
            sort_p.popleft()
        else:
            q.rotate(-1)  # 꼬리로 보내
    return answer