from collections import Counter, defaultdict
from itertools import combinations
def solution(orders, course):
    orders = [sorted(order) for order in orders]

    all_combinations = []
    freq_dict = defaultdict(list)
    for order in orders:
        for i in range(2, len(order) + 1):  # w/i order
            all_combinations.extend(set(combinations(order, i)))

    counter = Counter(all_combinations)
    for k, v in counter.items():
        if v >= 2:   # v: freq
            freq_dict[v].append(k)

    result = []
    freq_dict = sorted(freq_dict.items(), reverse=True)
    for i in course:
        found = False
        while not found:
            for _, menus in freq_dict:
                for menu in menus:
                    if len(menu) == i:
                        found = True
                        result.append(menu)
                if found: break
            found = True
    answer = sorted(["".join(i) for i in result])

    return answer