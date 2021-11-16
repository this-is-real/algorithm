def solution(phone_book):
    phone_book.sort()
    answer = True
    for idx in range(len(phone_book) - 1) :
        if phone_book[idx] == phone_book[idx + 1][:len(phone_book[idx])] :
            answer = False
            break
    return answer