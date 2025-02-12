"""
Exercise Week6 E3:
 * sätta in pengar (deposit)
 * ta up pengar (withdraw)
 * returnera nuvarande saldo (balance)
 * räkna ut ränta (apply_interest, lägger till räntan till kontot)
 * tala om ifall man har råd att betala en räkning (returnera True/False)
"""

class Bank():
    """
    A class to handle an account and do different things to the amount that the account holds.
    """
    
    # Default för att sätta upp class
    def __init__(self, amount: int | float) -> None:
        """
        Setup of the amount in the account.
        """
        if not isinstance(amount, (int, float)):
            self.__amount = 0.00
            
        else:
            self.__amount = float(amount)

    
    # Getter för balance of the amount in the account
    @property
    def balance(self):
        """
        Returns the current amount in the account.
        """
        return round(self.__amount, 2)
    
    
    # Method to deposit an amount
    def deposit(self, deposit: int | float) -> float:
        """
        Adds (deposit) an amount to the account.
        Returns the updated current balance.
        """
        if isinstance(deposit, (int, float)):
            self.__amount += deposit
        
        return self.balance
    
    
    # Method to withdraw an amount
    def withdraw(self, withdraw: int | float) -> None | float:
        """
        Removes (withdraw) an amount from the account.
        Returns 'None' if the withdraw is not possible, if possible it returns the updated current balance.
        """
        if not isinstance(withdraw, (int, float)):
            return None
        
        if self.balance - withdraw < 0:
            return None
        
        self.__amount -= withdraw
                
        return self.balance
    
    
    # Method for adding a rate
    def add_intrest_rate(self, rate: int | float) -> float:
        """
        Calculates an amount from the intrest rate and adds it to your account.
        Returns 0.00 if no intrest is possible, otherwise it returns the earned intrest amount.
        """
        if not isinstance(rate, (int, float)):
            return 0.00
        
        amount_rate = round(self.balance * (rate/100), 2)
        
        if amount_rate > 0:
            self.deposit(amount_rate)
            return amount_rate
        
        return 0.00
        
        
    # Method to check if a specifi invoice can be paid
    def check_invoice(self, invoice_amount: int | float) -> bool:
        """
        Checks to see if an invoice can be payed with the current amount.
        Returns only 'True' or 'False' if the invoice can be payed.
        """
        if not isinstance(invoice_amount, (int, float)):
            return False
        
        if self.balance - invoice_amount >= 0:
            return True
        
        return False
        
        
        
        