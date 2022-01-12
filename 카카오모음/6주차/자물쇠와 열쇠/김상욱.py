import math
import numpy as np

"""
    1. 전수조사 해야할듯..
    2. Lock의 오른쪽 아래 모서리(N,N)와 Key의 왼쪽위(1,1) 점을 맞대고
    3. Lock를 회전 (4회) -> Key는 남아도 되는 반면 Lock은 꼭 들어맞아야해서 Lock을 회전시킴
    4. 오른쪽(아래)로 한칸 이동후 확인
    5. 3~4 반복
"""

# 회전 - zip(* arrays[::-1]) 회전 시키는 코드
def rotated(arrays):
    rotate_arrays = zip(* arrays[::-1])
    return [list(i) for i in rotate_arrays]

# 일치여부 체크
def validation(key, lock):
    return np.logical_xor(key, lock).all()

def solution(key, lock):
    answer = False

    key = np.array(key)
    lock = np.array(lock)

    big_key = np.zeros((2*len(lock)+len(key)-2, 2*len(lock)+len(key)-2))
    big_key[len(lock)-1:len(big_key)-len(lock)+1, len(lock)-1:len(big_key)-len(lock)+1] = key

    for i in range(0, len(big_key)-len(lock)+1):
        for j in range(0, len(big_key)-len(lock)+1):
            for k in range(4):
                if validation(big_key[i:i+len(lock), j:j+len(lock)], lock):
                    return True
                lock = rotated(lock)

    return answer