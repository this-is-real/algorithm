from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

def get_pos(val):
    global keypad
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == val:
                return [i, j]

def get_dist(num, pos):
    global keypad
    visited = [[False for _ in range(3)] for _ in range(4)]
    visited[pos[0]][pos[1]] = True
    queue = deque([[*pos, 0]]) # [x, y, distance]
    total_dist = 0
    while queue:
        x, y, dist = queue.popleft()
        if keypad[x][y] == num:
            total_dist = dist
            break
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < 4 and 0 <= yy < 3 and not visited[xx][yy]:
                queue.append([xx, yy, dist+1])
    return total_dist

def get_hand_by_dist(left_dist, right_dist, hand):
    res = ""
    if left_dist < right_dist:
        res = "L"
    elif left_dist > right_dist:
        res = "R"
    else:
        res = "L" if hand == "left" else "R"
    return res

def solution(numbers, hand):
    answer = []
    left, right = [3, 0], [3, 2]
    for number in numbers:
        if number in [1, 4, 7]:
            left = get_pos(number)
            answer.append("L")
        elif number in [3, 6, 9]:
            right = get_pos(number)
            answer.append("R")
        else: # [2, 5, 8, 0]
            left_dist = get_dist(number, left)
            right_dist = get_dist(number, right)
            now_hand = get_hand_by_dist(left_dist, right_dist, hand)
            if now_hand == "L":
                left = get_pos(number)
            else:
                right = get_pos(number)
            answer.append(now_hand)
            
    return "".join(answer)