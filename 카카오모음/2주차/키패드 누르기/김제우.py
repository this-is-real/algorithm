def solution(numbers, hand):
    answer = ''
    left_keys = [1,4,7,'*']
    right_keys = [3,6,9,'#']
    center_keys = [2,5,8,0]
    left_pos = [0,3]
    right_pos = [2,3]
    for number in numbers:
        if number in left_keys:
            answer += "L"
            left_pos = [0,left_keys.index(number)]
        elif number in right_keys:
            answer += "R"
            right_pos = [2,right_keys.index(number)]
        elif number in center_keys:
            target_pos = [1,center_keys.index(number)]
            left_len = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_len = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            if left_len == right_len :
                if hand == "left":
                    answer += "L"
                    left_pos = target_pos
                else :
                    answer += "R"
                    right_pos = target_pos
            elif left_len > right_len :
                answer += "R"
                right_pos = target_pos
            else:
                answer += "L"
                left_pos = target_pos
    return answer