def solution(genres, plays):
    answer = []
    genres_cnt = {}
    for i in range(len(genres)):
        answer.append([i, genres[i], plays[i]])

        if genres_cnt.get(genres[i]):
            genres_cnt[genres[i]] += plays[i]
        else:
            genres_cnt[genres[i]] = plays[i]

    genres_rank = sorted(list(genres_cnt.keys()), key=lambda x: genres_cnt[x])
    answer.sort(key=lambda x: (genres_rank.index(x[1]), x[2], -x[0]), reverse=True)

    rank_cnt = {genre: 0 for genre in genres_cnt.keys()}
    res = []
    for i in answer:
        if rank_cnt[i[1]] < 2:
            rank_cnt[i[1]] += 1
            res.append(i[0])
    return res
