class BankAccount:
    def __init__(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass


# Dessa krav gäller för klassen BankAccount:
# 1. När klassen skapas, ska saldot vara 0
# 2. Saldot ska sparas privat i klassen, man ska använda en funktion för att
# hämta aktulellt värde
# 3. Deposit lägger till ett tal till saldot
# 4. Deposit ignorerar talvärden <= 0
# 5. Withdraw drar ifrån till ett tal från saldot
# 6. Withdraw ignorerar talvärden <= 0 och talvärden som är större än saldot
