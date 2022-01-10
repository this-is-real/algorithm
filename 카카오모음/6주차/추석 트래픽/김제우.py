import re
def solution(lines):
    new_lines = []
    for line in lines:
        end_time = re.findall(r'(\d{2,3})',line.split()[1])
        end_time = int(end_time[0]) * 60 * 60 + int(end_time[1]) * 60 + int(end_time[2]) + float(f"0.{end_time[3]}")
        duration = float(line.split()[2][:-1])
        start_time = end_time - duration
        new_lines.append((start_time, end_time))
    
    
    counts = []
    for line in new_lines:
        count = 0
        for line2 in new_lines:
            line_end = line[1]
            line_end_1 = line[1] + 1
            line2_end = line2[1]
            line2_start = line2[0]
            if line == line2:
                count += 1
            elif line2_start < line_end_1-0.001 and line_end <= line2_end:
                count += 1
        counts.append(count)
    answer = max(counts)
    return answer