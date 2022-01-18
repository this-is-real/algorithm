from itertools import permutations
import re
"""
    1. len(user_id)가 8로 매우 작음 + 효율성 없음
    2. 가능한 모든 Case 조사로 접근
    3. 순열로 만들면 banned_id 각 자리에 따른 모든 경우가 나옴
    4. 각 자리에 대해 정규표현식을 활용해 일치여부를 체크하고, 모든 자리에 일치하면 set에 담아준다.
    5. 그냥 set(set())은 오류가 발생 -> set(frozenset())으로 하면 가능 
    6. 5번처럼 담긴 set은 중복이 없으므로 len(set())이 정답
"""
def is_valid(user_id, banned_id):
    return len(user_id) == len(banned_id) and bool(re.compile(banned_id.replace('*', '.')).match(user_id))

def solution(user_id, banned_id):
    answer = set()
    
    for i in permutations(user_id, len(banned_id)):
        is_matched = True
        
        for user, banned in zip(i, banned_id):
            if not is_valid(user, banned):
                is_matched = False
                break
                
        if is_matched:
            answer.add(frozenset(i))

    return len(answer)