def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        a = [s for s in stages if s >= i]
        b = [s for s in stages if s == i]
        answer.append((i, 0 if not a else len(b) / len(a)))
    answer = sorted(answer, key=lambda x: -x[1])
    answer = [ans for ans, _ in answer]
    return answer