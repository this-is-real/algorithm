def solution(str1, str2):
    answer = 0
    str1_list = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_list = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    inter = []
    union = str1_list
    
    for i in str1_list:
        if i in str2_list:
            inter.append(i)
            str2_list.remove(i)
    union += str2_list
    if len(union) == 0 : return 65536
    else: return int(len(inter)/len(union)*65536)
