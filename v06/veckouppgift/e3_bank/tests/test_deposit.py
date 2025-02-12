"""
Krav: "sätta in pengar (deposit)"

User Story: "Som användare vill jag kunna sätta in pengar på mitt konto så att pengar kan öka"

Acceptanskriterier
 * När jag lägger till en summa pengar skall jag automatsik få tillbaka hur mycket jag har

Ytterligare krav
 * Sätta in belopp i både int och float
 * Skall få tillbaka i float avrundat i 2 siffror
 * Om icke godkänt tal skallläggas till skall bara balansen komma tillbaka
 * Väljer att inte att retunera något annat än balansen
"""

import pytest
from e3_bank.bank import *

@pytest.mark.parametrize("amount, deposit, expected_balance", [(100, 100, 200), 
                                                               (0.00, 10, 10.0), 
                                                               (1.00, 1.11, 2.11), 
                                                               (-10, 20, 10.0), 
                                                               (100, "", 100)])
def test_deposit__add_to_the_balance(amount, deposit, expected_balance):
    b = Bank(amount)
    
    assert b.deposit(deposit) == expected_balance