import random


class BankAccount():


    def __init__(self):
        self.account_number = ""
        self.name = None
        self.balance = 0
        self.valid_accounts = {}

    def create_new(self):
        print("Please enter your name: ")
        self.name = input()
        print("Please enter your initial deposit: ")
        self.balance += int(input())
        for x in range(5):
            self.account_number += str(random.randint(0, 9))
        print("Congratulations your account has successfully been created.  Your account number is {}"
              .format(self.account_number))
        self.valid_accounts[self.account_number] = self.name
        account.main_menu()

    def another_transaction(self):
        print("Would you like to perform another transaction? Y or N")
        user_input = input()
        if user_input.upper() == "Y":
            account.account_menu()
        else:
            quit()

    def deposit(self):
        print("Enter how much you want to deposit: ")
        self.balance += int(input())
        print("Current balance after deposit: ", self.balance)
        account.another_transaction()

    def withdraw(self):
        print("Enter how much you want to withdraw: ")
        self.amount = int(input())
        if self.balance <= 0:
            print("no funds to withdraw")
            account.account_menu()
        if self.amount > self.balance:
            print("insufficient funds")
            account.withdraw()
        else:
            self.balance -= self.amount
        print("Balance after withdraw: ", self.balance)
        account.another_transaction()

    def display(self):
        print("Your current balance is: ", self.balance)
        account.another_transaction()

    def validate(self):
        print("Enter your name: ")
        user_name = input()
        print("Enter your account number: ")
        user_account = input()
        if user_account in self.valid_accounts:
            if user_name == self.valid_accounts[user_account]:
                account.account_menu()
            else:
                print("invalid account")
                account.main_menu()

    def main_menu(self):
        print("To open a new account, Enter 1: \nTo access an existing account, Enter 2: ")
        option = int(input())
        if option == 1:
            account.create_new()
        elif option == 2:
            account.validate()

    def account_menu(self):

        while True:
            print("Enter 1 to make a deposit\nEnter 2 to withdraw\nEnter 3 to display balance\nEnter 4 to exit: ")
            action = int(input())

            if action == 1:
                account.deposit()
            elif action == 2:
                account.withdraw()
            elif action == 3:
                account.display()
            elif action == 4:
                quit()


account = BankAccount()
account.main_menu()


