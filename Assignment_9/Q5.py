
def checkDivisible(Value1):
    Result = False
    
    if Value1 % 5 == 0 and Value1 % 3 == 0:
        Result = True
    else:
        Result = False
        
    return Result

def main():
   ret = False
   
   print("Enter first no.")
   No1 = int(input())
   
   ret = checkDivisible(No1)
   
   if(ret):
        print("Divisible by 3 and 5")
   else:
        print("Not divisible by 3 and 5")
   

if __name__ == "__main__":
    main()