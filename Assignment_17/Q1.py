from Arithmetic import add,mult,sub,div

def main():

    No1 = int(input("Enter a number : "))
    No2 = int(input("Enter a number : "))

    Add = add(No1, No2)
    print("Addition of given number is : ", Add)

    Mult = mult(No1, No2)
    print("Multiplication of given number is : ", Mult)

    Sub = sub(No1, No2)
    print("Substraction of given number is : ", Sub)

    Div = div(No1, No2)
    print("Division of given number is : ", Div)

if(__name__ == "__main__"):
    main()