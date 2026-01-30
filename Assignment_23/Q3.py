class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self, isChePrime):
        increament = 1
        count = 0
        SumOfFactor = 0

        while (increament <= self.Value):

            if(self.Value % increament == 0):
                count = count + 1
                SumOfFactor = SumOfFactor + increament
            
            increament = increament + 1

        if(isChePrime):
            if(count == 2):
                print(True)
            else:
                print(False)

        return SumOfFactor

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value, 1):
            if(self.Value % i == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            print(True)
        else:
            print(False)

    def Factors(self):
        print("Factors of 5 are below : ")

        for i in range(1, self.Value+1, 1):
            if(self.Value % i == 0):
                print(i)

    def SumFactors(self):
        
        SumOfAllFactors = Numbers.ChkPrime(self, False)

        return SumOfAllFactors

ob1 = Numbers(5)

ob1.ChkPrime(True)
ob1.ChkPerfect()
ob1.Factors()

ret = ob1.SumFactors()
print("Sum of all factors is : ", ret)


