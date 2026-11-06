# Ewallet - Python Wallet App

A simple digital wallet built in Python by **Bayangbe Naibe**.

## Features
- Check balance
- Deposit money
- Withdraw money
- View transaction history

## Installation
```bash
git clone https://github.com/Little-Squid611/Ewallet.git
cd Ewallet
pip install -r requirements.txt
from wallet import Ewallet

my_wallet = Ewallet("Bayangbe Naibe")
my_wallet.deposit(100)
my_wallet.withdraw(30)
my_wallet.check_balance()
my_wallet.show_history()
Wallet for Bayangbe Naibe | Balance: $0.0
Deposited $100. New balance: $100.0
Withdrew $30. New balance: $70.0
