"""
  IDEA: 전수조사하기
  STEP
    1) Weak 갯수를 자연수 분할로 나눠준다. (ex 4 : [4], [3,1], [2,2], [2,1,1], [1,1,1,1])
    2) 조합으로 집합을 부분집합으로 나누는 모든 Case를 추출한다.
        ex) [1,5,6,10] -> [
          [[1,5,6,10]] # 4
          [[1,5,6],[10]],[[1,5,10],[6]],[[1,6,10],[5]][[5,6,10],[1]] # [3,1]
          [[1,5],[6,10]],[[1,6],[5,10]],[[1,10],[5,6]] # [2,2]
          [[1,5],[6],[10]],[[1,6],[5],[10]],[[1,10],[5],[6]]
          [[5,6],[1],[10]],[[5,10],[1],[6]],[[6,10],[1],[5]] # [2,1,1]
          [[1],[5],[6],[10]] #[1,1,1,1]
          ]
        check) 여기서 [1,6],[5,10]은 연속되지 않아서 사실 체크할 필요가 없지만 어차피 다른게 더 작은 값이 나와서 괜찮다.
       2-1) 자연수 분할 알고리즘 combinations_with_replacement
       2-2) 리스트를 set으로 바꾸고(어차피 중복값 없으므로), 재귀를 통해 위 case를 구한다.
    3) 각 집합에서 최소 거리를 구한다.
        ex) [[1,5,6],10] -> [5,8,11]: 5, [10]:1 [5,1]
    4) 최소거리 집합을 크기역순으로 정렬하고 dist와 비교하며 큰것부터 매칭시켜 모두 확인되면 return
      => 큰것부터 매칭되는 식이 아니라 answer = min()으로 업데이트
    5) 큰 순서대로 체크를 하기때문에 바로 return해도 되며, 자연수 분할의 크기가 dist의 크기보다 커지면 -1을 return

    2)번 하는 쉬운 방법이 있을거같은데 잘 모르겠다..
    => https://stackoverflow.com/questions/19368375/set-partitions-in-python
       역시 있다...
"""
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset
        yield [ [ first ] ] + smaller

def get_min_distance(part, n):
    temp_list = []

    for lst in part:
        if len(lst) == 1:
            temp_list.append(1)
            continue

        min_dist = lst[-1] - lst[0]
        for i in range(1, len(lst)):
            min_dist = min(min_dist, n - (lst[i] - lst[i-1]))
        temp_list.append(min_dist)

    return temp_list

def is_valid(dist, min_dist):
    min_dist.sort(reverse=True)

    for i in range(len(min_dist)):
        if dist[i] < min_dist[i]: return False

    return True

def solution(n, weak, dist):
    answer = len(dist)
    valid = False
    dist.sort(reverse=True)
    
    for part in partition(weak):
        if len(part) > len(dist):
            continue
            
        if is_valid(dist, get_min_distance(part, n)):
            valid = True
            answer = min(answer, len(part))

    return answer if valid else -1