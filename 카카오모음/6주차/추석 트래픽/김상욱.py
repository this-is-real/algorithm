from datetime import datetime, timedelta
import heapq

def convert_date_fromto(lines):
    # 입력값을 (작업시작, 작업끝) 형태로 변형해준다.
    result = []
    for line in lines:
        split_line = line.split(' ')
        to_dt = datetime.strptime(' '.join(split_line[:2]), '%Y-%m-%d %H:%M:%S.%f')
        from_dt = to_dt + timedelta(seconds=-float(split_line[2][:-1]) + 0.001)

        result.append((from_dt, to_dt))
        
    return result
    
def solution(lines):

    """
        핵심 아이디어
          1. 작업 시작시간으로 정렬한 배열 (input)
          2. 작업 종료시간을 적재하는 우선순위 큐 (가장 빨리 끝나는 작업 순으로 처리해야하므로) (heap)
          3. (1)(2)를 활용하여 우선순위 큐의 크기가 최대가 되는 순간의 값을 찾기
    """
    # 1. 주어진 데이터는 처리완료 시점기준 정렬이므로 시작시간 기준으로 재배열하기
    # 2. 첫번째 데이터의 종료시간을 우선순위 큐 heap에 넣어주기
    # 3. 다음 input 데이터와 큐안에 있는 가장 작은 종료시간을 비교해서 해당 시점으로부터 1초 안에 있는 값들을 우선순위 큐에 담기
    # 4. 만약 큐안에 있는 값이 더 작았다면 마지막에 heap의 크기로 최대크기여부를 판단한 후 해당 값 꺼내주기
    # 5. heap이 비어있다면 다음 input데이터 넣어주기
    # 6. 3~5 반복
    # 7. input이 비었다면 최대크기보다 더 커질수 없으니까 while문 빠져나오기

    answer = 1
    heap = []
    
    converted_lines = convert_date_fromto(lines)
    converted_lines.sort() # 시작 시간을 기준으로 정렬
    
    heap.append(converted_lines.pop(0)[1])

    while(converted_lines):
        from_dt, _ = converted_lines[0]

        if heap[0] < from_dt:
            time = heap[0] + timedelta(seconds=1 - 0.001)
        else:
            time = from_dt + timedelta(seconds=1 - 0.001)
            heapq.heappush(heap, converted_lines.pop(0)[1])
        
        while(converted_lines):
            if converted_lines[0][0] <= time:
                heapq.heappush(heap, converted_lines.pop(0)[1])
            else:
                break
        
        answer = max(answer, len(heap))
        
        if heap[0] < from_dt:
            heapq.heappop(heap)
        
        if (not heap) and converted_lines:
            heap.append(converted_lines.pop(0)[1])
    
    return answer

    """
        다른사람 풀이를 보고나서 생각해보니 굳이 우선순위 큐를 만들지 않고, 시작시간로 정렬한 배열과 종료시간으로 정렬한 배열
        두가지로 index를 옮겨가면서 진행하면 됬었겠다 싶었습니다...ㅎㅎㅎ
    """