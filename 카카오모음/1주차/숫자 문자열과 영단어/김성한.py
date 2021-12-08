import re

def solution(s):
    eng2num = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    result = re.findall("[0-9]{1}|" + "|".join(eng2num.keys()), s)
    result = [eng2num[r] if r in eng2num.keys() else r for r in result]
    return int("".join(result))