def make_row(n, number):
    row = []
    while True :
        rest = number%2
        row.append(rest)
        number = number//2
        if number == 0:
            break
    if len(row) < n :
        for item in range(n - len(row)):
            row.append(0)
    reverse_row = []
    for item in row:
        reverse_row.insert(0,item)
    return reverse_row
def solution(n, arr1, arr2):
    arr1_rows = []
    arr2_rows = []
    for item in arr1 :
        row = make_row(n,item)
        arr1_rows.append(row)
    for item in arr2 :
        row = make_row(n,item)
        arr2_rows.append(row)

    output = []
    for i in range(n):
        row = ""
        for item in zip(arr1_rows[i],arr2_rows[i]):
            if item[0] or item[1] == True:
                row += "#"
            else :
                row += " "
        output.append(row)
 
    answer = output
    return answer