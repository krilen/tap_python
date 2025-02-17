from utils import calculate_interest

class FakeBankAccount:
    balance = 0.0

    def deposit(self, amount):
        self.balance += amount


def test_calculate_interests():
    # förbereda testet
    account = FakeBankAccount()
    account.balance = 1000.0
    expected = account.balance * 1.05

    # anropa funktionen som ska testas
    calculate_interest(account)

    # kontrollera resultatet
    actual = account.balance
    assert actual == expected
