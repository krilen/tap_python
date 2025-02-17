
def calculate_interest(account):
    old_balance = account.balance
    interest = 0.05 * old_balance
    account.deposit(interest)


# Dessa krav gäller för calculate_interest:
# 1. Funktionen ska ignorera felaktiga värden på parametern
# 2. Funktionen ska räkna ut korrekt ränta, och anropa klassmetoden deposit
# (Funktionen ska öka saldot på kontot med räntesatsen)

