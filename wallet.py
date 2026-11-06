 class Ewallet:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0
        self.history = []

    def check_balance(self):
        print(f"Wallet for {self.owner_name} | Balance: ${self.balance}")
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Montant invalide ! Le dépôt doit être > 0")
            return False
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Montant invalide !")
            return False
        if amount > self.balance:
            print("Solde insuffisant !")
            return False
        self.balance -= amount
        self.history.append(f"Withdrew ${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True

    def show_history(self):
        print(f"--- Historique de {self.owner_name} ---")
        for h in self.history:
            print(h)

# --- TESTING THE WALLET ---
if __name__ == "__main__":
    my_wallet = Ewallet("Bayangbe Naibe")
    my_wallet.check_balance()
    my_wallet.deposit(100)
    my_wallet.deposit(50)
    my_wallet.withdraw(30)
    my_wallet.check_balance()
    my_wallet.show_history()
