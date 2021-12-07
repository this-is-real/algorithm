import re
def solution(new_id):
    #1. 소문자
    new_id = new_id.lower() 
    
    # 2. 알파벳 소문자, 숫자, -, _, . 빼고 모두 제거
    new_id = re.sub('[^0-9a-z_.-]', '',new_id)
    
    # 3.  연속 ..이면 .으로
    new_id = answer = re.sub('\.\.+', '.', new_id)
    
    # 4. 양쪽 . 제거
    if new_id[0] == '.' and len(new_id)>1:
        new_id = new_id[1:]
        
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5
    if len(new_id) == 0:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7 
    while len(new_id) < 3:
        new_id += new_id[-1:]
        
    answer = new_id
    return answer
