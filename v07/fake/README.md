# Kodexempel: mocking

## Struktur

Filen main.py är programmets startpunkt. Startfilen ska vara så liten som möjligt. Man bör strukturera sin kod så att så mycket som möjligt ligger i funktioner utanför main.py. Dessutom kan vi inte testa funktioner inuti main.py eftersom pytest inte tycker om funktionen input.

bank_account.py innehåller klassen BankAccount.

utils.py innehåller funktionen calculate_interest, som behöver testas med hjälp av mocking.
