"""
Krav: "returnera nuvarande saldo (balance)"

User Story: "Som användare vill jag kunna fråga så att jag får reda på hur mycket pengar jag har på mitt konto"

Acceptanskriterier
 * När jag frågar om balansen på mitt konto skall jag få totalen tillbaka
 
Ytterligare krav
 * Skall vara en python getter
 * En float skall retuneras vid alla tillfällen, avrundat till 2 decimaler
 * Skall vara möjligt att ha negativa tal
"""

import pytest
from e3_bank.bank import *

@pytest.mark.parametrize("amount, expected_balance", [(100, 100.00), 
                                                      ("", 0.00), 
                                                      (0, 0.00), 
                                                      (1.11, 1.11), 
                                                      (-12, -12.00)])
def test_balance__getting_the_current_balance(amount, expected_balance):
    b = Bank(amount)
    assert b.balance == expected_balance
    
    