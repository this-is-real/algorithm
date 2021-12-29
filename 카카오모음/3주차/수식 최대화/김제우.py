def op(string, number1, number2):
    if string == "*":
        return int(number1) * int(number2)
    elif string == "-":
        return int(number1) - int(number2)
    elif string == "+":
        return int(number1) + int(number2)
    
def solution(expression):
    depth1 = expression.split("+")
    depth2 = []
    for item in depth1:
        depth2.extend(item.split("-"))

    depth3 = []
    for item in depth2:
        depth3.extend(item.split("*"))

    operators = ""
    for item in expression :
        if not item.isdecimal():
            operators += item
            

    operator_orders = ["*-+","*+-","-*+","-+*","+*-","+-*"]
    new = []
    for i,item in enumerate(depth3):
        new.append(item)
        if i != len(depth3) -1 :
            new.append(operators[i])
    start = new[3:]
    stage = new[:3]
    result = []
    for oper_order in operator_orders:
        print(oper_order)
        result_temp = new
        for oper_now in oper_order:
            print(oper_now)
            start = result_temp[3:]
            stage = result_temp[:3]
            result_temp = []
            while start:
                print('start',start)
                print('stage',stage)
                print('result',result_temp)
                print('----')
                if oper_now in stage :
                    stage = [op(stage[1],stage[0],stage[2])]   
                else :
                    result_temp.extend(stage[:2])
                    stage = [stage[2]]
                stage.extend(start[:2])
                start = start[2:]
            print('start',start)
            print('stage',stage)
            print('result',result_temp)
            result_temp.extend(stage)
            # print('rt',result_temp)
        result_num = op(result_temp[1],result_temp[0],result_temp[2])
        result.append(result_num)
        print(result)
        
            
                

    # print(start)
    # new = []
    # for oper_order in operators:
    #     temp = [] 
    #     for i,number in enumerate(depth3):
    #         temp.append(number)
    #         if i != 0:
    #             temp.append(oper_order[i-1])
    #     new.append(temp)
    # print(new)
                
    # start = depth3     
    # for oper_order in operator_orders:
    #     #oper_order = "-+*"
    #     for oper_now in oper_order:
    #         stage = []
    #         result = []
    #         while operators:
    #             for i, operator in enumerate(operators):  #operators = "-*+-"
    #                 if i == 0:
    #                     if start :
    #                         number = start.pop(0)
    #                         stage.append(number)
    #                 if start :
    #                     number = start.pop(0)
    #                     stage.append(number)
    #                     if operator == oper_now:
    #                         stage = [op(operator, stage.pop(0),stage.pop(0))]
    #                     else :
    #                         result.append(stage.pop(0))
    #             operators = operators.replace(oper_now,'')
    #         result.extend(stage)
    #         start = result
            
                    
                
            
            
    answer = 0
    return answer