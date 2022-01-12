"""
    1. 도착 시간 정렬하기
    2. 막차 시간 계산하기
    3. 막차 시간에 탑승한 인원의 수가 m보다 작으면 막차시간에 콘이 도착 / 탑승한 인원의 수가 m과 같으면 해당 시간 -1분
"""
def solution(n, t, m, timetable):
    answer = 0
    timetable_min = []
    
    for i in timetable:
        hh, mm = i.split(':')
        minute = int(hh) * 60 + int(mm)
        timetable_min.append(minute)
    
    timetable_min.sort()
    crew_array = []
    
    for i in range(n):
        crew = 0

        while timetable_min:
            if timetable_min[0] <= 540 + (t * i): # 09:00 -> 540분
                answer = timetable_min.pop(0)
                crew += 1

                if crew == m: break
            else:
                break

        crew_array.append(crew)

    if crew_array[-1] == m:
        answer = answer - 1
    else:
        answer = 540 + (t * (n-1))

    hh, mm = divmod(answer, 60)
    answer = str(hh).rjust(2, "0") + ':' + str(mm).rjust(2, "0")

    return answer