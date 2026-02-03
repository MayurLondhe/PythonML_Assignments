import os

def main():
    
    FileName = input("Enter a file name : ")
    Ret = os.path.exists(FileName)

    if(Ret):
        print(f"{FileName} exists.")
    else:
        print(f"{FileName} not exixts.")
    

if(__name__ == "__main__"):
    main()