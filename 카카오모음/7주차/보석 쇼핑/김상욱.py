from collections import defaultdict
"""
    1. two pointer 문제로 생각하고 포인터를 이동해가면서 경우에 맞는 케이스 찾기
    2. 모든 보석이 담겨야하므로 R포인터를 증가시키면서 모든 보석이 담기도록 하고
    3. 모든 보석이 담긴 시점부터는 L포인터를 증가시켜서 작은 영역으로 담기도록 한다.
    4. 2~3 과정을 반복하면서 가장 최적의 영역을 추출
"""
def solution(gems):
    
    answer = [0, len(gems)]
    
    gem_set = set(gems)
    gem_dict = defaultdict(int)
    
    point_L, point_R = 0, 0
    moved_R = True
    
    if len(gem_set) == 1: return [1, 1]
    
    while point_R < len(gems):
        if moved_R:
            gem_dict[gems[point_R]] += 1
            moved_R = False

        # 모든 종류의 보석이 담겼을 때
        if len(gem_dict) == len(gem_set):
            if answer[1] - answer[0] > point_R - point_L:
                answer[0] = point_L
                answer[1] = point_R

            if gem_dict[gems[point_L]] == 1:
                del gem_dict[gems[point_L]]
            else:
                gem_dict[gems[point_L]] -= 1

            point_L += 1

        else:
            point_R +=1
            moved_R = True

    answer[0] += 1
    answer[1] += 1
    
    return answer