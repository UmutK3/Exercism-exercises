def answer(question):
    question = question.lower()
    if not question.startswith("what is") or not question.endswith("?"): #Checking the question is in the correct form.
        raise ValueError("unknown operation")
    question = question[7:-1].strip() #Removing unnecessary parts of the problem
    question = question.replace("divided by","divided")
    question = question.replace("multiplied by","multiplied")
    process = question.split()
    if not process:
        raise ValueError("syntax error")
    try:
        value = int(process[0]) #Checking if the initial value is a number.
    except ValueError:
        raise ValueError("syntax error")
    operation_number = 1
    while operation_number < len(process):
        if operation_number + 1 >= len(process): #Checking whether there is a value after the operation type
            if all(process_type not in process for process_type in ["plus","minus","divided","multiplied"] ):
                raise ValueError("unknown operation") #If these two conditions are met, there is an invalid operation.For example What is 5 Cubed ? 
            raise ValueError("syntax error") #If only the first condition is met, this is a syntax error.
        try:
            number = int(process[operation_number + 1]) #Checking the value after the operation type
        except ValueError:
            raise ValueError("syntax error")
        if process[operation_number] == "plus":
            value += number
        elif process[operation_number] == "minus":
            value -= number
        elif process[operation_number] == "divided":
            value /= number
        elif process[operation_number] == "multiplied":
            value *= number
        else:
            raise ValueError("unknown operation") #If the above conditions are not met, the operation is invalid.
        operation_number += 2
    return value




    