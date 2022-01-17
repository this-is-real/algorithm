# 테스트 케이스 5번: 5637.06ms

from itertools import product

def solution(user_id, banned_id):
    answer = []
    n = len(banned_id)
    candidates = [[] for _ in range(n)]
    
    for idx, b_id in enumerate(banned_id):
        target_ids = [u_id for u_id in user_id if len(u_id) == len(b_id)]
        for target_id in target_ids:
            is_match = True
            for t, b in zip(target_id, b_id):
                if b == "*":
                    continue
                if t != b:
                    is_match = False
                    break
            if is_match:
                candidates[idx].append(target_id)
    
    for candidate in product(*candidates):
        obj = set(candidate)
        if len(obj) == n and obj not in answer:
            answer.append(obj)
    
    return len(answer)