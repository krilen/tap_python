


class Account():
    """
    A class to handle an account
    """
    
    def __init__(self, name: str, 
                        amount: int = 0, 
                        rate: float = 0.0, 
                        comment: str = "") -> None:
        self.name = name
        self.amount = amount
        self.rate = rate

if __name__ == "__main__":
    print("Wrong file!!!")