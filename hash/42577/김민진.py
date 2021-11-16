from collections import defaultdict

def solution(phone_book):
    phone_dict = defaultdict(list)
    for i in phone_book:
        phone_dict[i[0]].append(i)

    for i in "123456789":  # 1 ~ 9
        phone_dict[i] = sorted(phone_dict[i])
        for j in range(1, len(phone_dict[i])):
            if phone_dict[i][j-1] == phone_dict[i][j][:len(phone_dict[i][j-1])]:
                return False
    return True
    