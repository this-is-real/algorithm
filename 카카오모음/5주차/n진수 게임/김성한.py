def convert(num, base):
    special = {i+10: chr(i+65) for i in range(6)} # 10:A, 11:B, ...
    res = []
    while num > 0:
        num, r = divmod(num, base)
        res.append(str(r) if r not in special else special[r])
    return ''.join(reversed(res))

def solution(n, t, m, p):
    num_list = []
    for num in range(t*m):
        converted_num = convert(num, n) if num else num
        num_list.extend(list(str(converted_num)))
    target_idx = [m*i+p-1 for i in range(t)] # 등차수열
    answer = "".join([num for idx, num in enumerate(num_list) if idx in target_idx])
    return answer