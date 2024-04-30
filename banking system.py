class BankAccount:
    def __init__(self,name,account_number,pass_code,balance=0):
        self.name = name
        self.account_number = account_number
        self.pass_code = pass_code
        self.balance = balance
    def account_login(self):
        account_number = int(input('Enter your account number:'))
        pass_code = int(input('Enter your pass code:'))
        if account_number==self.account_number and pass_code==self.pass_code:
            print('Login successfully!hi',self.name)
        else:
            print('Invalid input')
    def deposit(self):
        amount = int(input('Enter the depositing amount:'))
        self.balance += amount
        print('Transaction successful available balance:',self.balance)
    def withdraw(self):
        amount = int(input('Enter the withdrawal amount:'))
        pass_code = int(input('Enter your pass code:'))
        self.balance -= amount
        if amount > self.balance:
            print('Insufficient balance')
        else:
            print('Transaction successful')
    def check_balance(self):
         print('Current balance is:',self.balance)

bank = BankAccount('Sanu',10111213,465987,0)
bank.account_login()
bank.deposit()
bank.withdraw()
bank.check_balance()

