import itertools
def is_prime(n):
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

def solution(numbers):
        
    numbers = [i for i in numbers]
    
    p_list = []
    for index in range(1,len(numbers)+1):
        p_list.append(list(itertools.permutations(numbers, index)))
    
    prime_list = []
    for item in p_list:
        for tup in item:
            string = ''
            for j in tup:
                string += j
            if is_prime(int(string)):
                prime_list.append(int(string))
                
    while 1 in prime_list:
        prime_list.remove(1)
    while 0 in prime_list:
        prime_list.remove(0)

    prime_list = list(set(prime_list))

    answer = len(prime_list)
    return answer