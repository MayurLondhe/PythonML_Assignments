
def ChkGreater(Value1, Value2):
    if Value1 > Value2:
        print("Greater number is : ", Value1)
    else:
        print("Greater number is : ", Value2)

def main():
   No1 = 0
   No2 = 0
   
   print("Enter first no.")
   No1 = int(input())
   print("Enter second no.")
   No2 = int(input())
   
   ChkGreater(No1, No2)

if __name__ == "__main__":
    main()