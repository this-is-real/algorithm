def solution(phone_book):
    sorted_nums = sorted(phone_book)
    
    for idx in range(len(sorted_nums)-1):
        pointer = sorted_nums[idx]
        
        if pointer == sorted_nums[idx+1][:len(pointer)]:
            return False
        
    return True
