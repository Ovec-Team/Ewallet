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
  
# Taux de change (base : 1 unité de la devise = X XAF)
TAUX_XAF = {
    "XAF": 1,
    "EUR": 655.957,
    "USD": 600,
    "GBP": 760,
}


def convert(montant, devise_source, devise_cible):
    """Convertit un montant d'une devise vers une autre."""
    devise_source = devise_source.upper()
    devise_cible = devise_cible.upper()

    if montant < 0:
        raise ValueError("Le montant doit être positif.")
    if devise_source not in TAUX_XAF or devise_cible not in TAUX_XAF:
        raise ValueError("Devise non supportée.")

    # On passe par le XAF comme devise pivot
    montant_xaf = montant * TAUX_XAF[devise_source]
    resultat = montant_xaf / TAUX_XAF[devise_cible]
    return round(resultat, 2)
