class Budget:
    def __init__(self):
        self.food = 10000
        self.clothing = 2000
        self.entertainment = 50000

    def deposit(self):
        print("NOTE: INPUT IS CASE SENSITIVE")
        categories, amount = input('Which category do you want to deposit "food", "clothing",'
                                   ' "entertainment"? '), int(input("How much would you like to deposit? "))
        if categories == "food":
            self.food += amount
            print(f"Your balance now is {self.food}")
        elif categories == "clothing":
            self.clothing += amount
            print(f"Your balance now is {self.clothing}")
        else:
            self.entertainment += amount
            print(f"Your balance now is {self.entertainment}")

    def withdraw(self):
        print("NOTE: INPUT IS CASE SENSITIVE")
        categories = input('Which category do you want to withdraw from "food", "clothing", "entertainment"? ')
        if categories == "food":
            amount = int(input("How much do you want to withdraw? "))
            if self.food < amount:
                print("Insufficient Funds, please deposit")
            else:
                print(f"Take your {amount} cash")
                self.food -= amount
                print(f"Your balance is {self.food}")
        elif categories == "clothing":
            amount = int(input("How much do you want to withdraw? "))
            if self.clothing < amount:
                print("Insufficient Funds")
            else:
                print(f"Take your {amount} cash")
                self.clothing -= amount
                print(f"Your balance is {self.clothing}")
        else:
            amount = int(input("How much do you want to withdraw? "))
            if self.entertainment < amount:
                print("Insufficient Funds")
            else:
                print(f"Take your {amount} cash")
                self.entertainment -= amount
                print(f"Your balance is {self.entertainment}")

    def checkBalance(self):
        print("NOTE: INPUT IS CASE SENSITIVE")
        balance = input('Which category would you like to check balance \n-food\n-clothing\n-entertainment? ')
        if balance == "food":
            print(self.food)
        elif balance == "clothing":
            print(self.clothing)
        else:
            print(self.entertainment)

    def transfer_balance(self):
        print("NOTE: INPUT IS CASE SENSITIVE")
        From = input("Which category would you like to transfer from food, clothing, entertainment? ")
        if From == "food":
            To = input("Which category would you like to transfer balance to clothing or entertainment ")
            if To == "entertainment":
                self.entertainment += self.food
                self.food = 0
                print(f"Your entertainment balance is {self.entertainment} and food balance is {self.food}")
            else:
                self.clothing += self.food
                self.food = 0
                print(f"Your clothing balance is {self.clothing} and food balance is {self.food}")

        elif From == "Cloth":
            To = input("Which category would you like to transfer balance to food or Entertainment ")
            if To == "food":
                self.food += self.clothing
                budget.clothing = 0
                print(f"Your food balance is {self.food} and cloth balance is {self.clothing}")
            else:
                self.entertainment += self.clothing
                self.clothing = 0
                print(f"Your entertainment balance is {self.entertainment} and cloth balance is {self.clothing}")
        else:
            To = input("Which category would you like to transfer balance to food or clothing ")
            if To == "clothing":
                self.clothing += self.entertainment
                self.entertainment = 0
                print(f"Your clothing balance is {self.clothing} and entertainment is {self.entertainment}")
            else:
                self.food += self.entertainment
                budget.entertainment = 0
                print(f"Your food balance is {self.food} and entertainment is {self.entertainment}")


budget = Budget()

# To DEPOSIT CASH ( Change the amount to deposit by editing it)
budget.deposit()

# TO WITHDRAW CASH
budget.withdraw()

# COMPUTING BALANCE
budget.checkBalance()

# TRANSFER BALANCE BETWEEN CATEGORIES
budget.transfer_balance()
