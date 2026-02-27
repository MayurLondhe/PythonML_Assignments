from Q1 import Load_csv

def main():
    df = Load_csv("student_performance_ml.csv")
    print("Dataset gets loaded successfully...")

    PassCount = 0
    FailCount = 0

    for value in df["FinalResult"]:
        if(value == 1):
            PassCount = PassCount + 1
        else:
            FailCount = FailCount + 1

    print(PassCount)
    print(FailCount)

if(__name__ == "__main__"):
    main()