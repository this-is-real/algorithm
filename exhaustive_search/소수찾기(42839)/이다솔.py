def solution(numbers):
    from itertools import permutations
    numbers = list(numbers)
    all_nums = [list(permutations(numbers, n)) for n in range(1, len(numbers) + 1)] # 모든 경우의 수 구하기
    final = []
    for number in all_nums :                                                        # 모든 조합을 합쳐 숫자로 넣기
        final += [int(''.join(n)) for n in number if n]
    final = sorted(list(set(final)))                                                # 중복 삭제, 오름차순 정렬
    answer = []
    for num in final :                                                              # 하나씩 소수인지 판별
        prime = True
        if num < 2 :
            continue
        for i in range(2, int(num ** 0.5) + 1) :                                    # 그 수의 제곱근까지 나누어보면서
            if num % i == 0 :                                                       # 나누어 떨어지면 False
                prime = False
                break
        answer.append(prime)
    return answer.count(True)                                                       # True 개수 세서 반환
