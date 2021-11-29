def solution(operations):
    import heapq
    dual_q = []
    heapq.heapify(dual_q)

    for op in operations :
        if 'I' in op :                                        # I가 있으면
            heapq.heappush(dual_q, int(op[2:]))               # 해당 숫자를 heap에 추가
        elif op == "D 1" and dual_q :                         # 최대값을 빼야할 때는 (비어있는 heap인 경우 명령 무시)
            dual_q = heapq.nlargest(len(dual_q), dual_q)[1:]  # 내림차순으로 정렬하여 2번째 요소부터 빼오기
            heapq.heapify(dual_q)                             # 다시 heapify
        elif op == "D -1" and dual_q :                        # 최솟값을 빼야할 때는 (비어있는 heap인 경우 명령 무시)
            heapq.heappop(dual_q)                             # heappop

    if not dual_q :                                           # heap이 비어있다면 [0, 0] 반환
        return [0, 0]
    else :                                                    # 비어있지 않다면 [최대값, 최솟값] 반환
        return [heapq.nlargest(1, dual_q)[0], heapq.heappop(dual_q)]
    