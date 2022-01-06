def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {alphabet[i-1]:i for i in range(1,27)}
    answer = []
    i = 0
    while i<=len(msg)-1:
        msg_list = [item for item in msg][i:]
        w = "".join(msg_list)
        if msg_list :
            while True:
                if w in dictionary:
                    break
                msg_list.pop()
                w = "".join(msg_list)
        answer.append(dictionary[w])
        if i+len(w) < len(msg):
            dictionary[w+msg[i+len(w)]] = len(dictionary)+1
        i += len(w)
    return answer