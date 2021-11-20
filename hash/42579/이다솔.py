def solution(genres, plays):
    from collections import defaultdict
    answer = []
    total_plays = defaultdict(int)
    best_albums = defaultdict(list)

    for idx in range(len(genres)):
        total_plays[genres[idx]] += plays[idx]
        best_albums[genres[idx]].append((idx, plays[idx]))
    total_plays = sorted(total_plays.items(), key=lambda x : -x[1])

    for song in total_plays :
        play = sorted(best_albums[song[0]], key=lambda x : -x[1])
        for idx in range(len(play)) :
            if idx >= 2 :
                break
            answer.append(play[idx][0])

    return answer