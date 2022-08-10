def arithmetic_arranger(lista,true=False):   
    #1 Situations that will return an error
    if len(lista)>5:
        return "Error: Too many problems."

    str_lista=" ".join(lista)
    new_lista=str_lista.split()

    operators=[]
    strs=[]
    counter=0
    up_numbers=[]
    down_numbers=[]
    lines=[]
    total_operation=[]

    for operator in new_lista:
        if operator=="+" or operator=="-":
            operators.append(operator)
            continue
        if operator.isdigit()==True:
            counter+=1
            if len(operator)>4:
                #4 Situations that will return an error
                return "Error: Numbers cannot be more than four digits."

            if counter%2!=0:
                up_numbers.append(operator)
            else:
                down_numbers.append(operator)
            continue
        else:
            strs.append(operator)

    #2 Situations that will return an error
    if len(operators)<len(lista):
        return "Error: Operator must be '+' or '-'."

    #3 Situations that will return an error
    if len(strs)>=1:
        return "Error: Numbers must only contain digits."

    #calculating the lines width and the total of the math operations.
    results=0
    width_line=0
    counter_lines=0
    spaces=4
    for up_number,down_number,operation in zip(up_numbers,down_numbers,operators):
        counter_lines+=1
        if len(up_number)>=len(down_number):
            width_line=(len(up_number)+2)*"-"
        if len(down_number)>=len(up_number):
            width_line=(len(down_number)+2)*"-"
        lines.append(width_line)

        if operation=="+":
            results=int(up_number)+int(down_number)
        if operation=="-":
            results=int(up_number)-int(down_number)
        total_operation.append(results)

    #finding the right space
    counter=1
    up_numbers_space,up_numbers_sp=0,[]
    down_numbers_space,down_numbers_sp=0,[]
    lines_space,lines_sp=0,[]
    total_operation_space,total_operation_sp=0,[]
    for upspace,downspace,operatorspace,linespace,totalspace in zip(up_numbers,down_numbers,operators,lines,total_operation):
        counter+=1
        totalspace=str(totalspace)
        spacio=" "

        #for up_numbers
        if len(lista)>=1:
            up_numbers_space=((len(linespace))-len(upspace))*spacio
            up_numbers_sp.append(up_numbers_space)
            up_numbers_sp.append(upspace)

        #space after operation
        if counter<=len(lista):
            up_numbers_sp.append(spaces*spacio)

        #for down_numbers
        if (len(linespace)>len(downspace)):
            #to add the operator
            down_numbers_sp.append(operatorspace)
            down_numbers_space=((len(linespace)-len(downspace))-1)*spacio
            down_numbers_sp.append(down_numbers_space)
            down_numbers_sp.append(downspace)

        #space after operation
        if counter<=len(lista):
            down_numbers_sp.append(spaces*spacio)
            
        #for lines spaces
        if len(lista)>=1:
            lines_space=spaces*spacio
            lines_sp.append(linespace)
        if counter<=len(lista):
            lines_sp.append(lines_space)

        #for total_operation
        if (len(linespace)>=len(totalspace)):
            total_operation_space=((len(linespace))-len(totalspace))*spacio
            total_operation_sp.append(total_operation_space)
            total_operation_sp.append(totalspace)

        #space after operation
        if counter<=len(lista):
            total_operation_sp.append(spaces*spacio)

    up_numbers_str="".join(map(str,up_numbers_sp))
    down_numbers_str="".join(map(str,down_numbers_sp))
    lines_str="".join(map(str, lines_sp))
    total_operation_str="".join(map(str,total_operation_sp))

    out=[up_numbers_str.rjust(len(lines_str)),down_numbers_str.rjust(len(lines_str)),lines_str]

    if true==True:
        out.append(total_operation_str.rjust(len(lines_str)))

    output = "\n".join(out)

    return output
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))