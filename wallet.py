class Ewallet:
    def__init__(Self, owener_name):
       self.owner_name = owner_name
       self.balance = 0.0
    def check_balance(self):
        print(f"wallet for {self.owner_name}| balance:${self.balance}")
    def deposit(self,amount):
        if amount <= 0:
            print("le montant doit etre positif.")
            return
        self.balance +=amount
        print(f"deposited ${amount}.new balance: ${self.balance}")
  #----TESTING THE WALLET----
  if__name__== "__main__":
     my_wallet = Ewallet("forchu shalom")
     my_wallet.check_balance()
     my_wallet.deposit(50)  