import sys
sys.setrecursionlimit(10**6)

def preorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    answer.append(node[2])
    if len(arrY1) > 0:
        preorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer)
    return

def postorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])
    return

def solution(nodeinfo):
    preanswer = []
    postanswer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    arrX = sorted(nodeinfo)
    
    preorder(arrY, arrX, preanswer)
    postorder(arrY, arrX, postanswer)
    
    return [preanswer, postanswer]