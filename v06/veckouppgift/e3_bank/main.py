"""
3 Banken
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
 * sätta in pengar (deposit)
 * ta up pengar (withdraw)
 * returnera nuvarande saldo (balance)
 * räkna ut ränta (apply_interest, lägger till räntan till kontot)
 * tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.

Använder ovastående punkter som de grundläggande kraven från kunden 

"""

from bank import *

def main():
        
    # Balance
    b1 = Bank(10)
    
    print(f"My balance in 'b1': {b1.balance}")
    
    b2 = Bank(9.99)
    print(f"My balance in 'b2': {b2.balance}")
    
    print()
    
    
    # Deposit
    add1 = 33
    b1.deposit(add1)
    print(f"Depositing: {add1}, making my balance: {b1.balance}")
    
    add2 = 2.44
    b2.deposit(add2)
    print(f"Depositing: {add2}, making my balance: {b2.balance}")

    print()

    # Withdraw
    remove1 = 10
    b1.withdraw(remove1)
    print(f"Withdrawing: {remove1}, making my balance: {b1.balance}")
    
    remove2 = 6.67
    b2.withdraw(remove2)
    print(f"Withdrawing: {remove2}, making my balance: {b2.balance}")
    
    print()
    
    # Intrest rate
    rate1 = 2.3
    print(f"Add {rate1}% intrest rate gives me {b1.add_intrest_rate(rate1)} more, making my balance: {b1.balance}")
    
    rate2 = 0.9
    print(f"Add {rate2}% intrest rate gives me {b2.add_intrest_rate(rate2)} more, making my balance: {b2.balance}")
        
    print()
    
    # Check payable invoice
    invoice1 = 50
    print(f"With the balance of {b1.balance} can I pay an invoice of {invoice1}? - {'Yes' if b1.check_invoice(invoice1) else 'No'}")
    
    invoice2 = 3.33
    print(f"With the balance of {b2.balance} can I pay an invoice of {invoice2}? - {'Yes' if b2.check_invoice(invoice2) else 'No'}")
    
if __name__ == "__main__":
    
    
    
    main()