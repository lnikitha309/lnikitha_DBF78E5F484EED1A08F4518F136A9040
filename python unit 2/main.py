class BankAccount:
    def __init__(self, account_number, account_holder_name,      initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance:${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")
    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient funds to make the withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (ACCOUNT NUMBER) #{self.__account_number}: ${self.__account_balance}")
if __name__ == "__main__":
    my_account = BankAccount(123456789, "John Doe", 1000)
    my_account.display_balance()
    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.withdraw(1500)
    my_account.display_balance()
