import os
import sys

def CopyFileContentAndInsert(FileName):
        fobj = open(FileName,"r")

        Data = fobj.read()

        CreatedFileName = "Demo1.txt"

        fobj1 = open(CreatedFileName,"w")

        fobj1.write(Data)

        fobj.close()
        fobj1.close()

        print(f"Created {CreatedFileName} and copyed contents of {FileName} into {CreatedFileName}")

def main():
    
    if(len(sys.argv) != 2):
        print("Invalid input parameters.")
        return
        
    Ret = os.path.exists(sys.argv[1])

    FileName = sys.argv[1]

    if(Ret):
        CopyFileContentAndInsert(FileName)
    else:
        print(f"{FileName} not exixts.")
    

if(__name__ == "__main__"):
    main()