import re
def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id = re.sub(r"[^-_.a-z0-9]","",new_id)
    #3단계
    new_id = re.sub(r"[.]+",".",new_id)
    #4단계 -> strip으로 하자...
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
        
    #5단계
    if new_id == "":
        new_id += "a"
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    #7단계 -> for문 말고 곱하기를 쓰자...
    if len(new_id) <= 2:
        for i in range(3-len(new_id)):
            new_id += new_id[-1]
    answer = new_id
    return answer