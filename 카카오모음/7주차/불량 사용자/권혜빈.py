def solution(user_id, banned_id):
    answer = []
    candidates = [[]]
    for b_id in banned_id:
        new_candidates = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            check = True
            for i in range(len(u_id)):
                if b_id[i] != '*' and u_id[i] != b_id[i]:
                    check = False
                    break
            if check:
                for c in candidates:
                    if u_id not in c:
                        new_candidates.append(c+[u_id])
        candidates = new_candidates
    print(candidates)
    for c in candidates:
        if set(c) not in answer:
            answer.append(set(c))
