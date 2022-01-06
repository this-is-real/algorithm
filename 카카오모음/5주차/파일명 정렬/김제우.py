import re
def solution(files):
    result = []
    for file in files:
        temp = re.findall(r'(^[A-Za-z .-]*)(\d{1,5})(.*)',file)
        result.extend(temp)

    output = {}
    for i, item in enumerate(result):
        if item[0].lower() in output:
            output[item[0].lower()].append((item[1],item[2],i))
        else :
            output[item[0].lower()] = [(item[1],item[2],i)]
    
    for key,val in output.items():
        output[key] = sorted(val, key = lambda x: int(x[0]))
    
    r = []
    for key in sorted(output.keys()):
        r.extend(output[key])
    answer = [files[i[2]] for i in r]

    return answer