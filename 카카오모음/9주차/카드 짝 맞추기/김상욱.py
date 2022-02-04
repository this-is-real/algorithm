# 1. 같은 카드의 좌표를 묶음으로 표시할 것.
# 2. 전체 배열의 경우의 수 순열을 구하기.
#   2-1. A -> A`와 A`-> A 가 다름
# 3. BFS를 활용하여 모든 경우에 대해 최단 거리 이동수를 계산
# 4. 3으로부터 나온 결과 중 최단거리가 정답.
# https://tiktaek.tistory.com/68 코드 가져옴...
# 풀이 이해만 해보기

from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy
def move_cost(board, start, end):   # 조작 횟수 Count
    if start==end: return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:                    # BFS
        x, y, c = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1))
                visit.add((cx, cy))

def cls_cost(board, cdict, curr, order, cost):
    if len(order)==0: return cost   # 모든 카드를 확인한 경우
    idx = order[0]+1                # 현재 선택해야할 카드의 종류

    # 현재위치에서 A1까지의 조작 횟수 + A1->A2까지의 조작 횟수 + 2(카드 선택)
    choice1 = move_cost(board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:   # 적은 조작 횟수를 한 경우를 따라 재귀
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)

def solution(board, r, c):
    answer = float('inf')
    cdict = defaultdict(list)
    for row in range(4):        # 카드의 종류에 따라 좌표 저장
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)):    # 완전 탐색
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer