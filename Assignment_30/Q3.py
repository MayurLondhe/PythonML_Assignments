import os
import sys

def ReadDataLineByLine(FileName1):
        fobj = open(FileName1,"r")

        Data = fobj.readlines()

        for i in range(0, len(Data), 1):
             print(Data[i])
        
        fobj.close()

def main():
    
    if(len(sys.argv) != 2):
        print("Invalid input parameters.")
        return
        
    FileExists = os.path.exists(sys.argv[1])

    FileName = sys.argv[1]

    if(FileExists):

        ret = ReadDataLineByLine(FileName)

    else:
        print("file not exixts.")
    

if(__name__ == "__main__"):
    main()