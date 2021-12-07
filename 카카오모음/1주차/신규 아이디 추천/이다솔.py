def solution(new_id):
    ID = ''
    # 1, 2 단계
    new_id = new_id.lower()
    for alpha in new_id :
        if alpha.isalnum() or alpha in '-_.' :
            ID += alpha

    # 3, 4 단계
    while '..' in ID :
        ID = ID.replace('..', '.')
    if ID.startswith('.') : 
        ID = ID[1:]
    if ID.endswith('.') :
        ID = ID[:-1]
        
    # 5, 6, 7 단계
    if not ID :
        ID = 'a'  
    if len(ID) > 15 :
        ID = ID[:15]
        if ID[-1] == '.' :
            ID = ID[:-1]          
    if len(ID) <= 3 :
        ID += ID[-1] * (3 - len(ID))
        
    return ID
