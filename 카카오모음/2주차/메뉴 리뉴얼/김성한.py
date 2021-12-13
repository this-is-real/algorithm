from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i, course_cnt in enumerate(course):
        menus = []
        for order in orders:
            for menu in combinations(order, course_cnt):
                menus.append(''.join(menu))
        menus = [''.join(sorted(list(menu))) for menu in menus]
        counter = Counter(menus)
        if not counter:
            continue
        max_cnt = max([cnt for cnt in counter.values()])
        if max_cnt == 1:
            continue
        target = [menu for menu, cnt in counter.items() if cnt == max_cnt]
        answer.extend(target)
    answer.sort()
    return answer