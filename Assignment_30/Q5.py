import os
import sys

def CheckWordIsPresentInFile(FileName1, StringName):
        fobj = open(FileName1,"r")

        Data = fobj.read()
        Data = Data.split(" ")

        Ret = False

        for i in range(0, len(Data), 1):
            if(StringName == Data[i]):
                Ret = True
                continue
                 
            
        fobj.close()
        return Ret

def main():
    
    if(len(sys.argv) != 3):
        print("Invalid input parameters.")

        print("-"*50)
        print("-"*50)

        print("Follow below instruction")
        print(f"{sys.argv[0]} Argument1 Argument2")
        print("Argument1 : Exixting File Name.")
        print("Argument2 : Word to check whether this word is present in file or not.")

        print("-"*50)
        print("-"*50)

        return
        
    FileExists1 = os.path.exists(sys.argv[1])

    FileName1 = sys.argv[1]
    Word = sys.argv[2]

    if(FileExists1):

        ret = CheckWordIsPresentInFile(FileName1, Word)

        if(ret):
            print(f"{Word} is found in {FileName1}.")
        else:
            print(f"'{Word}' is not found in {FileName1}.")

    else:
        print("File not exixts.")
    

if(__name__ == "__main__"):
    main()