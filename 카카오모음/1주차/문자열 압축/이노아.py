def solution(s):
    answer = 0
    
    # exception case 
    if len(s) == 1:
        return 1
    
    # search from 1 to len(s)//2
    for n in range(1, len(s)//2+1):
        sliced = [s[i:i+n] for i in range(0,len(s),n)]      # string slice
        candidate = ''                                      # answer candidate
        multiple = 1                                        # initialize

        for i in range(1,len(sliced)):
            if sliced[i] == sliced[i-1]:                    # if repeated
                multiple += 1
            elif sliced[i] != sliced[i-1]:                  # if repeated x
                if multiple == 1:
                    candidate += sliced[i-1]
                else:
                    candidate += str(multiple)+sliced[i-1]
                multiple = 1
        
            if i == len(sliced)-1:                          # last slice concat
                if multiple > 1:
                    candidate += str(multiple)+sliced[i]
                else:
                    candidate += sliced[i]

        if answer > len(candidate) or answer == 0:          # comparison retain min
            answer = len(candidate)

    return answer