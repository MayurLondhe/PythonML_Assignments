class Arithmetic:
    PI = 3.14

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        print("Enter the two values of Arithmatic")
        self.Value1 = int(input())
        self.Value2 = int(input())

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans
        

    def Subtraction(self):
        Ans = self.Value1 - self.Value2
        return Ans
        
    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans

    def Divisible(self):
        Ans = 0
        try:

            Ans = self.Value1 / self.Value2

        except ZeroDivisionError:
            print("Unable to divide by zero.")

        return Ans

objArithmetic = Arithmetic()

objArithmetic.Accept()

Ret = objArithmetic.Addition()
print("Addition of given numbers is : ", Ret)

Ret = objArithmetic.Multiplication()
print("Multiplication of given numbers is : ", Ret)

Ret = objArithmetic.Subtraction()
print("Subtraction of given numbers is : ", Ret)

Ret = objArithmetic.Divisible()
print("Divisible of given numbers is : ", Ret)

