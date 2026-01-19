
def squrt(Value1):
   Result = 0
   Result = Value1** 0.5
   
   return Result

def main():
   No1 = 0
   
   print("Enter no.")
   No1 = int(input())
   SquareRoot = squrt(No1)
   print("Square root of given number is : ", SquareRoot)
   

if __name__ == "__main__":
    main()