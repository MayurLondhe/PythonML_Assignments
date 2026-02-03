import os
import sys

def CopyFileContentAndInsert(FileName1, FileName2):
        fobj = open(FileName1,"r")

        Data = fobj.read()

        CreatedFileName = FileName2

        fobj1 = open(CreatedFileName,"w")

        fobj1.write(Data)

        fobj.close()
        fobj1.close()

        print(f"Contents of {FileName1} copied into {CreatedFileName}")

def main():
    
    if(len(sys.argv) != 3):

        print("Invalid input parameters.")

        print("-"*50)
        print("-"*50)

        print("Follow below instruction")
        print(f"{sys.argv[0]} Argument1 Argument2")
        print("Argument1 : Exixting File Name.")
        print("Argument2 : New File Name.")

        print("-"*50)
        print("-"*50)

        return
        
    FileExists1 = os.path.exists(sys.argv[1])

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if(FileExists1):
        CopyFileContentAndInsert(FileName1, FileName2)
    else:
        print("File not exixts.")
    

if(__name__ == "__main__"):
    main()