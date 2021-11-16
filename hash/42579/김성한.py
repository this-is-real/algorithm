# 성공

def solution(genres, plays):
    answer = []
    genre_total = {g: 0 for g in set(genres)}
    genre_songs = {g: [] for g in set(genres)}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
    
    genre_total = sorted([(g, p) for g, p in genre_total.items()], key=lambda x: -x[1])
    
    for g, _ in genre_total:
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        if len(songs) > 1:
            songs = songs[:2]
        answer.extend([i for _, i in songs])

    return answer