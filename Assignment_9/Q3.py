
def squrt(Value1):
   Result = 0
   Result = Value1 ** 2
   
   return Result

def main():
   No1 = 0
   
   print("Enter no.")
   No1 = int(input())
   Square = squrt(No1)
   print("Square of given number is : ", Square)
   

if __name__ == "__main__":
    main()