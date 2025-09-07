class BankAccount:
    bank_name = "State Bank"
    
    def __init__(self, name, account_no, branch, balance):
        self.name = name
        self.__account_no = account_no
        self._branch = branch
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Deposited amount is {amount}")
        else:
            print(f"Deposit amount should be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"Withdrawn amount is {amount}")
        else:
            print(f" Insufficient balance for withdrawal of {amount}")

    @property
    def account_no(self):
        return self.__account_no
    
    @property
    def branch(self):
        return self._branch
    
    @branch.setter
    def branch(self, new_branch):
        self._branch = new_branch
    
    @property
    def balance(self):
        return self.__balance
        
    def customer_info(self):
        print(f"Customer Name : {self.name}")
        print(f"Bank Name : {BankAccount.bank_name}")
        print(f"Branch Name : {self.branch}")
        print(f"Account Number : {self.account_no}")


account1 = BankAccount("Anil", 123456789, "Vijayanagar", 10000)
account1.customer_info()
account1.deposit(5000)
account1.withdraw(1000)
print(account1.balance)


account2 = BankAccount("Geetha", 123456788, "Kuvempunagar", 50000)
account2.customer_info()
account2.deposit(10000)
print(account2.balance)
account2.branch = "Vijaynagar"
account2.customer_info()
