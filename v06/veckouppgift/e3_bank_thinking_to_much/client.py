from typing import Any

class Client():
    """
    A class to handle multiple clients and their account this should connect to the DB
    """
    
    def __init__(self) -> None:

        # A single account: {..., <client>: [{ "name": <value>, "amount": <value>, "rate": <value>, "comment": <value>}, ...], ...}
        
        self.clients: dict[list[dict[Any]]] = {
                        "jack": [{"name": "basic", "amount": 100, "rate": 3.2},],
                        "sarah": [{"name": "basic","amount": 150, "rate": 3.1},],
                        }

    
    def get_client_account(self, client) -> dict[Any] | None:
        return self.clients.get(client, None) 
        
    def add_client(self, name: str) -> None:
        pass


if __name__ == "__main__":
    print("Wrong file!!!")