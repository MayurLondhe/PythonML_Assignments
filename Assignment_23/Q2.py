class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
        

    def Display(self):
        print(f"Name : {self.Name} || Current Balance : {self.Amount}")

    def Deposit(self):
        DepositAmount = int(input("Enter the amount for deposit : "))

        self.Amount = self.Amount + DepositAmount

    def Withdraw(self):
        WithdrawAmount = int(input("Enter the amount for withdraw : "))

        if(WithdrawAmount <= self.Amount):
            self.Amount = self.Amount - WithdrawAmount
        else:
            print("insufficient balance for withdraw.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

obj1 = BankAccount("Mayur Londhe",20000)

obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

