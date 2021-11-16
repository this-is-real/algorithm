# def solution(phone_book):
#     m = min(phone_book)
#     phone_book.remove(m)
    
#     for i in phone_book:
#         if m == i[:len(m)]:
#             return False
    
#     return True

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer
