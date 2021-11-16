# 성공
# 문자열을 정렬하면 접두어에 속하는 문자들끼리는 이어서 존재하게 된다.
# 따라서 인접한 두 개의 전화번호를 비교하면 된다.

def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True