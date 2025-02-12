"""
Krav: "räkna ut ränta (apply_interest, lägger till räntan till kontot)"

User Story: "Som användare vill jag få ränta på mina pengar så att det är värt att spara"

Acceptanskriterier
 * När jag tar ut en summa pengar skall jag automatiskt få tillbaka hur mycket jag har kvar

Ytterligare krav
 * Anger vilken ränta som skall användas, måste var en int eller float
 * Skall återanvända deposit metoden
 * Få tillbaka räntan som lagts på
 * Vid 0 eller mindre på kontot skall ingen ränta ges
"""

import pytest
from e3_bank.bank import *


@pytest.mark.parametrize("amount, rate, expected_amount_rate, expected_balance", [(0, 2.3, 0, 0), 
                                                                                  (100, 2.3, 2.3, 102.30),
                                                                                  (-10, 5, 0, -10),
                                                                                  (1.1, 1.2, 0.01, 1.11)])
def test_add_intrest_rate__add_intrest_to_the_balance(amount, rate, expected_amount_rate, expected_balance):
    b = Bank(amount)
    assert b.add_intrest_rate(rate) == expected_amount_rate
    assert b.balance == expected_balance