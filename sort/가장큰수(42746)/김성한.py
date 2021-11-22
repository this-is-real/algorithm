# 성공

def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    # 원소의 길이가 0~1000 이므로 3자리수로 만들어서 비교 정렬
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    # int -> str : 모든 숫자가 0인 경우(ex. 000)를 처리하기 위해
    answer = str(int(''.join(numbers)))
    return answer