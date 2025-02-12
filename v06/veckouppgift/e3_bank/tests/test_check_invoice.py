"""
Krav: "tala om ifall man har råd att betala en räkning (returnera True/False)"

User Story: "Som användare vill jag kunna kontrollera om jag kan betala en räkning så att räkningen betalas"

Acceptanskriterier
 * Jag skall kunna fråga om en specifik räkning kan betalas.
 
Ytterligare krav
 * Endast int/float som räkning
 * Ger endast True / Fasle som svar
"""

import pytest
from e3_bank.bank import *

@pytest.mark.parametrize("amount, invoice, payable", [(100, 110, False),
                                                      (0, 10, False),
                                                      (100, "", False),
                                                      (100, 10, True), 
                                                      (15.13, 15.13, True)])
def test_check_invoice__checking_payable_invoice(amount, invoice, payable):
    b = Bank(amount)
    assert b.check_invoice(invoice) == payable
    