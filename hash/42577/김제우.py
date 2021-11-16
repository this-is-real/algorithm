def make_dict(phone_book,item_len):
    phone_dict = {}
    for item in phone_book:
        if item[:item_len] in phone_dict :
            phone_dict[item[:item_len]].append(item[item_len:])
        else:
            phone_dict[item[:item_len]] = [item[item_len:]]
    return phone_dict
    
def solution(phone_book):
    answer = True
    dict_list = []
    for i in range(1,19):
        phone_dict = make_dict(phone_book, i)
        dict_list.append(phone_dict)
        for value in phone_dict.values():
            if len(value) != 1 and '' in value:
                answer=False
                break
    
    return answer