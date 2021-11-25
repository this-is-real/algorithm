def solution(brown, yellow):
    total = brown + yellow
    
    #공약수 찾기 -> frame 만들기
    frames = []
    for i in range(3,total//2):
        if total % i == 0 and i >= total//i:
            frames.append((i,total//i)) 
            
    answer = []
    for width, height in frames:
        brown_count = 0
        for i in range(width//2):
            brown_count += 2*(width-2*i) + 2*(height-2*i) - 4
            if brown_count == brown and width*height-brown_count == yellow:
                answer.append(width)
                answer.append(height)
    
    return answer