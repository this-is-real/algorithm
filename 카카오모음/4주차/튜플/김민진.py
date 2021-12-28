from collections import Counter

def solution(s):
    all_sets = eval(s[1:-1])  # str -> Tuple[Set]
    if isinstance(all_sets, set):
        all_sets = (all_sets,)

    # initialize counter
    counter = Counter()
    for a_set in all_sets:
        counter.update(a_set)

    answer = [k for k, _ in counter.most_common()]
    return answer
