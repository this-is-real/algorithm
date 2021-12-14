from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for leng_ in course:
        candidates = []
        for menus in orders:
            for combo in combinations(menus, leng_):
                combo_sorted = ''.join(sorted(combo))
                candidates.append(combo_sorted)
        max = Counter(candidates).most_common(1)[0][1]
        answer += [menu for menu, cnt in list(Counter(candidates).items()) if cnt >= 2 and cnt == max]
    return sorted(answer)