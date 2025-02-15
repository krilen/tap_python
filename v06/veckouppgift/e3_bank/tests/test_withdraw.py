"""
Krav: "ta up pengar (withdraw)"

User Story: "Som användare vill jag kunna ta ut pengar som finns på mitt konto"

Acceptanskriterier
 * När jag tar ut en summa pengar skall jag automatsik få tillbaka hur mycket jag har kvar
 * Skall inte kunna ta ut mer än vad jag har på kontot

Ytterligare krav
 * Ta ut belopp i både int och float
 * Skall få tillbaka balansen i float avrundat i 2 siffror
 * Om det inte är möjligt att ta ut beloppet skall None informera
"""

import pytest
from bank import *


@pytest.mark.parametrize("amount, withdraw, expected_balance", [(100, 50, 50.00), 
                                                                ("", 10, None), 
                                                                (0, 10, None), 
                                                                (1.11, 1.1, 0.01), 
                                                                (12, 15, None)])
def test_withdraw__remove_from_the_balance(amount, withdraw, expected_balance):
    b = Bank(amount)
    assert b.withdraw(withdraw) == expected_balance