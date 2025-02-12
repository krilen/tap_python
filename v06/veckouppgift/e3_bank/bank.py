"""
 * sätta in pengar (deposit)
 * ta up pengar (withdraw)
 * returnera nuvarande saldo (balance)
 * räkna ut ränta (apply_interest, lägger till räntan till kontot)
 * tala om ifall man har råd att betala en räkning (returnera True/False)
"""

class Bank():
    
    # Default för att sätta upp class
    def __init__(self, amount: int | float) -> None:
        
        if not isinstance(amount, (int, float)):
            self.__amount = 0.00
            
        else:
            self.__amount = float(amount)

    
    # Getter för balance of the amount in the account
    @property
    def balance(self):
        return round(self.__amount, 2)
    
    
    # Method to deposit an amount
    def deposit(self, _deposit: int | float) -> float:
        
        if isinstance(_deposit, (int, float)):
            self.__amount += _deposit
        
        return self.balance
    
    
    # Method to withdraw an amount
    def withdraw(self, _withdraw: int | float) -> None | float:
        if not isinstance(_withdraw, (int, float)):
            return None
        
        if self.balance - _withdraw < 0:
            return None
        
        self.__amount -= _withdraw
                
        return self.balance
    
    
    # Method for adding a rate
    def add_intrest_rate(self, rate: int | float) -> float:
        if not isinstance(rate, (int, float)):
            return 0.00
        
        amount_rate = round(self.balance * (rate/100), 2)
        
        if amount_rate > 0:
            self.deposit(amount_rate)
            return amount_rate
        
        return 0.00
        
        
    # Method to check if a specifi invoice can be paid
    def check_invoice(self, invoice_amount: int | float) -> bool:
        if not isinstance(invoice_amount, (int, float)):
            return False
        
        if self.balance - invoice_amount >= 0:
            return True
        
        return False
        
        
        
        