
fobj = open("Demo1.txt","r")

Data = fobj.read()

Data = Data.split(" ")

print(Data)

import os
import sys

def CountOfOccurences(FileName1, StringName):
        fobj = open(FileName1,"r")

        Data = fobj.read()
        Data = Data.split(" ")

        Count = 0

        for i in range(0, len(Data), 1):
             if(StringName == Data[i]):
                  Count = Count + 1
                  
        fobj.close()
        return Count

def main():
    
    if(len(sys.argv) != 3):
        print("Invalid input parameters.")
        return
        
    FileExists1 = os.path.exists(sys.argv[1])

    FileName1 = sys.argv[1]
    StringName = sys.argv[2]

    if(FileExists1):

        ret = CountOfOccurences(FileName1, StringName)

        print(f"{StringName} appears in {FileName1} is {ret} times.")
    else:
        print("Sum of ther file is not exixts.")
    

if(__name__ == "__main__"):
    main()