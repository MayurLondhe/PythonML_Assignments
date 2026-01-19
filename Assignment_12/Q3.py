
def addition(N1, N2):
    add = None

    add = N1+N2

    return add

def multiplication (N1, N2):
    mult = None

    mult = N1*N2

    return mult

def subtraction(N1, N2):
    sub = None
    sub = N1-N2
    return sub

def division(N1, N2):
    divi = None
    divi = N1/N2

    return divi

def main():

    print("Enter two numbers : ")

    Value1 = int(input())
    Valuer2 = int(input())

    print("Addition is :", addition(Value1, Valuer2))
    print("Subtraction is :", subtraction(Value1, Valuer2))
    print("Multiplication is :", multiplication(Value1, Valuer2))
    print("Division is :", division(Value1, Valuer2))

if __name__ == "__main__":
    main()