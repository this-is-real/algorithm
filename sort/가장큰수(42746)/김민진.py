def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = int(''.join(numbers))  # 0 이면
    return str(answer)
    