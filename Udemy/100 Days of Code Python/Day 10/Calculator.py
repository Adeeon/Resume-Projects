from CalcArt import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add, 
    '-': subtract, 
    '/':divide, 
    '*':multiply
}
def calculation():
    print(logo)
    end = False
    i = 0
    con_answer = 0
    while not end:
        if i == 0:
            num1 = float(input("What's the first number?: "))
            for key in operations:
                print(key)
            operation_symbol = input("Pick an operations from the lines above: ")
            num2 = float(input("What's the second number?: "))
            answer = operations[operation_symbol](num1, num2)
            print(f'{num1} {operation_symbol} {num2} = {answer}')
            repeat = input(f"""Type 'y' to coninue calculating with {answer}, or type 'n' to exit, 
            or 'r' to restart: """)
            if repeat == 'y':
                con_answer = answer
                i += 1
            elif repeat == 'r':
                calculation()
            else:
                end = True
        elif i != 0:
            operation_symbol = input('Pick an operations: ')
            next_num = float(input('Whats the next number?'))
            next_answer = operations[operation_symbol](con_answer, next_num)
            print(f'{con_answer} {operation_symbol} {next_num} = {next_answer}')
            repeat = input(f"""Type 'y' to coninue calculating with {answer}, or type 'n' to exit, 
            or 'r' to restart: """)
            if repeat == 'y':
                con_answer = next_answer
            elif repeat == 'r':
                calculation()
            else:
                end = True
calculation()

# def calculator():
#     print(logo)
#     end = False

#     num1 = float(input("What's the first number?: "))
#     for key in operations:
#         print(key)
#     while not end:
#         operation_symbol = input("Pick an operations from the lines above: ")
#         num2 = float(input("What's the second number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f'{num1} {operation_symbol} {num2} = {answer}')

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")== "y":
#             num1 = answer
#         else:
#             end = True
#             calculator()

 


# operation_symbol = input("Pick another operations: ")
# num3 = int(input("What's the third number?: "))
# second_answer = operations[operation_symbol](first_answer, num3)

# print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')