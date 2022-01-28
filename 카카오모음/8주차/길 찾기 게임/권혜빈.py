# 이해중
import sys
sys.setrecursionlimit(10 ** 6)

def order(nodeinfo, layer, cur_layer):
    global answer
    cur_node = nodeinfo.pop(0)
    answer[0].append(cur_node[2])

    if nodeinfo:
        for i in range(len(nodeinfo)):
            if nodeinfo[i][1] == layer[cur_layer + 1]:
                if nodeinfo[i][0] < cur_node[0]:
                    order([x for x in nodeinfo if x[0] < cur_node[0]], layer, cur_layer + 1)
                else:
                    order([x for x in nodeinfo if x[0] > cur_node[0]], layer, cur_layer + 1)
    answer[1].append(cur_node[2])


def solution(nodeinfo):
    global answer
    answer = [[], []]
    layer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
        if nodeinfo[i][1] not in layer:
            layer.append(nodeinfo[i][1])

    layer.sort(reverse=True)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    order(nodeinfo, layer, 0)

    return answer
