def addition(num1, num2):
    return (num1 + num2)

def substraction(num1, num2):
    return (num1 - num2)

def multiplication(num1, num2):
    return (num1 * num2)

def division(num1, num2):
    return (num1 / num2)


# define calc function
def calc(num1, num2, op_type='+'):
    if op_type == '+':
        return addition(num1, num2)
    elif op_type == '-':
        return substraction(num1, num2)
    elif op_type == '*':
        return multiplication(num1, num2)
    elif op_type == '/':
        return division(num1, num2)
    else:
        return

# define operate_calculator function
def operate_calculator():
    input1 = int(input("first number: "))
    input2 = int(input("second number: "))
    input3 = input("operator type (+, -, *, /): ")

    calc_result = calc(input1, input2, op_type = input3)

    if calc_result is None:
        print("wrong operator type.")
    else:
        print("%d %s %d = %s" %(input1, input3, input2, calc_result))

operate_calculator()