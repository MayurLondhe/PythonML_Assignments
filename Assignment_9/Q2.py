
def ChkGreater(Value1, Value2):
    Result = 0
    if Value1 > Value2:
        Result = Value1
    else:
        Result = Value2

    return Result

def main():
   No1 = 0
   No2 = 0
   
   print("Enter first no.")
   No1 = int(input())
   print("Enter second no.")
   No2 = int(input())
   
   ret = ChkGreater(No1, No2)

   print("Greater number is : ", ret)

if __name__ == "__main__":
    main()