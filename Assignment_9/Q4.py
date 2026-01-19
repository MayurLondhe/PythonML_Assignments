
def GetCube(Value1):
    Result = 0
    Result = Value1 ** 3
    
    return Result

def main():
   No1 = 0
   
   print("Enter first no.")
   No1 = int(input())
   
   ret = GetCube(No1)
   
   print("Cube of given number is : ", ret)

if __name__ == "__main__":
    main()