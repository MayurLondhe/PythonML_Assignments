import os
import sys

def CompareFileData(FileName1, FileName2):
        fobj = open(FileName1,"r")

        Data1 = fobj.read()

        fobj1 = open(FileName2,"r")

        Data2 = fobj1.read()

        if(Data1 == Data2):
            print("Success")

        else:
            print("Failure")

        fobj.close()
        fobj1.close()

def main():
    
    if(len(sys.argv) != 3):
        print("Invalid input parameters.")
        return
        
    FileExists1 = os.path.exists(sys.argv[1])
    FileExists2 = os.path.exists(sys.argv[2])

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if(FileExists1 and FileExists2):
        CompareFileData(FileName1, FileName2)
    else:
        print("Sum of ther file is not exixts.")
    

if(__name__ == "__main__"):
    main()