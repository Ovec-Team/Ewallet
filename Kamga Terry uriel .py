   class Ewallet:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0

    def check_balance(self):
        print(f"Wallet for {self.owner_name} | Balance: ${self.balance}")

  # ___ TESTING THE WALLET ___
  if __name__== "__main__":
      my_wallet = Ewallet("Forchu Shalom")
      my_wallet.check_balance()

      # TODO for teammates: Add a deposit function below!
 def deposit(self, amount):
     self.balance += amount
     print(f"Deposited ${amount}.New balance: ${self.balance}")

def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient funds.")
    else:
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
