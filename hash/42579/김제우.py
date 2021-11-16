def solution(genres, plays):
    album = {}
    for i,(genre,play) in enumerate(zip(genres,plays)):
        if genre not in album :
            album[genre] = [(i,play)]
        else :
            album[genre].append((i,play))
    
    genre_order = []
    for k,v in album.items():
        total=0
        for item in v :
            total += item[1]
        genre_order.append([k,total])
    
    result = sorted(genre_order,key=lambda x: x[1],reverse=True)
    
    answer = []
    for (genre,_) in result:
        for i,(num,_) in enumerate(sorted(album[genre],key=lambda x: x[1], reverse=True)):
            if i < 2 :
                answer.append(num)
            else :
                break
    
    return answer