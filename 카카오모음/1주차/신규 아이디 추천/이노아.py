import re

def solution(new_id):
    id = re.sub(r'[^a-z0-9-_.]', '', new_id.lower())    # Cond 1-2
    id = re.sub('\.+','.', id)                          # Cond 3
    id = id.strip('.')                                  # Cond 4
    
    if len(id) == 0:                                    # Cond 5
        id = 'a'
        
    if len(id) >= 16:                                   # Cond 6
        id = id[:15]
        id = id.strip('.')
        
    if len(id) <= 2:                                    # Cond 7
        id += id[-1]*2
        id = id[:3]
        
    return id