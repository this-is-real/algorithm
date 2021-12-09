def solution(s):
    n_eng = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    n_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for n in n_eng :
        if n in s :
            s = s.replace(n, n_str[n_eng.index(n)])
    return int(s)
