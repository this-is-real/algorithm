import re

def solution(files):
    answer = []
    splited_files = []
    for idx, file in enumerate(files):
        head, number, tail = re.findall(r"([A-Za-z .-]+)(\d+)([\dA-Za-z .-]*)", file)[0]
        splited_files.append((file, head.lower(), int(number), idx))
    splited_files.sort(key=lambda x: (x[1], x[2], x[3]))
    answer = [file[0] for file in splited_files]
    return answer