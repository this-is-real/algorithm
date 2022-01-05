def solution(msg):
    answer = []
    dic = {chr(i+65): (i+1) for i in range(26)}
    while msg:
        w = ""
        length = max([len(word) for word in dic])
        while True: # 가장 긴 w 찾기
            temp_w = msg[:length]
            if temp_w in dic:
                w = temp_w
                break
            length -= 1
        c = msg[length:length+1]
        answer.append(dic[w])
        dic[w+c] = max([idx for idx in dic.values()])+1
        msg = msg[length:]
    return answer