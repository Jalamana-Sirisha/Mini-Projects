def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
dict={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
def calculator():
    try :
        n1=input("Enter a number: ")
        number1=float(n1)
    except ValueError:
        print("Invalid input....enter the correct input ")

    for symbol in dict:
        print(symbol)
    continue_flag=True
    while  continue_flag :
        opr_symbol=input("pick an operator: ")
        try:
            n2=input("Enter a number : ")
            number2=float(n2)
        except ValueError:
            print("Invalid input")
        symbol_opr=dict[opr_symbol]
        output = symbol_opr(number1,number2)
        print(output)
        ans=input("Type 'y' or 'yes if you want continue or type 'n' or 'no' to discontinue: ")
        if ans=='y' or 'yes':
            number1=output
        elif ans=='n' or 'no':
            continue_flag=False
            print("Bye")

calculator()


