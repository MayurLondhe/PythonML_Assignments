
def Grade(Marks):
    Result = ""

    if(Marks >= 75):
        Result = "Distinction"
    elif (Marks >= 60):
        Result = "First Class"
    elif (Marks >= 50):
        Result = "Second Class"
    else:
        Result = "Fail"

    return Result

def main():
    
    MarksIn = int(input("Enter a marks : "))

    ret = Grade(MarksIn)

    print("Grage is : ", ret)


if __name__ == "__main__":
    main()