from colorama import init
from colorama import Fore
import time
import string


def typo_check(user_choice, option_word):
    # compares the user input to the menu option
    # determines if they are close enough to be accepted
    try:
        option_word = [i.lower() for i in option_word]
        for i in user_choice:
            if i.lower() in option_word:
                option_word.pop(option_word.index(i))
        if len(option_word) <= 1:
            return True
    except:
        return False


def name_check():
    # check for a valid F/L name before creating the account
    while True:
        client_first_name = input('Please enter the first name of the account holder: ').capitalize()
        client_last_name = input('Please enter the last name of the account holder: ').capitalize()
        invalid_name = False
        for i in list(client_first_name + client_last_name):
            if i.lower() not in string.ascii_lowercase:
                invalid_name = True
        if invalid_name == False:
            name_confirm = input(f'Is {client_first_name} {client_last_name} correct? Y/N: ')
            if name_confirm.lower() == 'y':
                return (client_first_name, client_last_name)



class BankAccount:

    def __init__(self,account_holder_name,balance=0.00):

        self.account_holder_name = ' '.join(list(account_holder_name))
        self.balance = balance
        self.first_name, self.last_name = account_holder_name[0], account_holder_name[1]


    def __str__(self):

        return f"\nAccountholder: {self.account_holder_name} \nBalance: ${format(self.balance, '.2f')}"


    def deposit(self, deposit_amount):

        self.balance += deposit_amount


    def withdraw(self, withdraw_amount):

        if self.balance - withdraw_amount > 0:
            self.balance -= withdraw_amount
        else:
            print('Insufficient funds.')


    def menu(self):

        # gives users the options to deposit/withdraw/exit, while keeping a running print of the balance
        # confirms numeric input to ensure that amounts are valid
        # prevents users from withdrawing more than the current account balance
        transaction_complete = False
        print(f'Welcome, {self.first_name}.')
        while transaction_complete == False:
            print(f"Your available balance is ${format(self.balance, '.2f')}.")
            choice = input('Would you like to make a DEPOSIT, a WITHDRAWAL, or EXIT?: ')
            if typo_check(choice, 'deposit'):
                amount = input('How much would you like to deposit? $')
                try:
                    self.deposit(float(amount))
                except:
                    print('Not a valid input.')
            elif typo_check(choice, 'withdrawal'):
                amount = input('How much would you like to withdraw? $')
                try:
                    self.withdraw(float(amount))
                except:
                    print('Not a valid input.')
            elif choice.lower() == 'exit':
                print(Fore.BLUE + 'Goodbye!' + Fore.RESET)
                transaction_complete = True
            else:
                print('Invalid input.')


if __name__ == '__main__':
    print("Welcome to Bank Name, preparing for account setup.")
    time.sleep(1)
    account = BankAccount(name_check())
    account.menu()


