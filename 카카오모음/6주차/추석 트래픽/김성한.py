def get_time(time):
    hour, minute, second = time.split(":")
    second, millisecond = second.split(".")
    hour = int(hour) * 3600
    minute = int(minute) * 60
    second = int(second)
    millisecond = int(millisecond)
    return (hour + minute + second) * 1000 + millisecond

def get_start_time(time, diff):
    diff = diff[:-1]
    diff = int(float(diff) * 1000)
    return get_time(time) - diff + 1

def solution(lines):
    answer = 0
    start_time, end_time = [], []

    for line in lines:
        _, end, diff = line.split(" ")
        start_time.append(get_start_time(end, diff))
        end_time.append(get_time(end))
    
    n = len(lines)
    for i in range(n):
        cnt = 0
        cur_time = end_time[i]
        for j in range(i, n):
            if cur_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer