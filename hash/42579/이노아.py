from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list) # genre -> [idx, play]
    dic_cnt = defaultdict(int) # genre -> plays_cnt
    answer = [] 
    
    for idx, genre, play in zip(range(len(plays)),genres,plays):
        # print(genre,play,idx)
        dic[genre] += [[idx, play]]
        dic_cnt[genre] += play
    
    # order keys in descending cnts
    for k in dict(sorted(dic_cnt.items(), key = lambda t: -t[1])).keys(): 
        # key1 : descending plays, key2 : ascending idx
        temp =  sorted(dic[k], key = lambda t: (-t[1], t[0])) 
        answer += temp[:2] # two songs per genre

    return [i[0] for i in answer] # return idx only
