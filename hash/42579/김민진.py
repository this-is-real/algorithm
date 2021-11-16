from collections import defaultdict

TOPK = 2

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    genre_count = defaultdict(int)
    for id, play in enumerate(plays):
        genre_dict[genres[id]].append((id, play))
        genre_count[genres[id]] += play
    
    genre_order = [i for i in genre_count.items()]
    genre_order.sort(key=lambda x:x[1], reverse=True)
    
    for item in genre_order:
        sorted_play = sorted(genre_dict[item[0]], key=lambda x:x[1], reverse=True)
        sorted_play_idx, _ = zip(*sorted_play)
        answer.extend(sorted_play_idx[:TOPK])
    
    return answer
    