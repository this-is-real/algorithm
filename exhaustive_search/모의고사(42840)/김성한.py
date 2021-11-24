# 성공

def solution(answers):
    answer = []
    ps = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    ans = [[p[i%len(p)] for i in range(len(answers))] for p in ps]
    for i, a in enumerate(ans):
        answer.append((i+1, sum([a1 == a2 for a1, a2 in zip(a, answers)])))
    max_cnt = max([ans[1] for ans in answer])
    answer = sorted([ans[0] for ans in answer if ans[1] == max_cnt])
    return answer