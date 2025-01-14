
is_member = False
level1 = 100
level2 = 300
discount = 0
"""
1. Vad är syftet med koden?
   > Ange ett pris och få ut ett nytt pris med eventuell rabatt
2. Testkör koden med några olika värden.
   > 100, 101, 301
3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
   > Ja, sista raden blander string med float genom "+"
4. Finns det logiska fel? (programmet gör något annat än det är tänkt)
   > Ja, Ordningen (och olika) på if satsen vid val av 300 fås båda rabatterna 25 + 10 => 30%
     Ändrat så att bara blir en if sats och ändrat ordningen
5. Diskutera möjliga lösningar på felen ni hittat.
   > Slå ihop och säkerställ orningen av vilkorskontrollen i if satsten
6. Diskutera möjliga förbättringar på koden
   > * Börja med att säkerställa vad man skall ge för input
     * Lägg till "kr" i output (även i input)
     * Endast output om rabatt om det blir rabatt.
        - ytterligare if stats om 'discount > 0'
"""

price = input("Välkommen, köp något dyrt, ange ett pris (kr): ")
price = float(price)

if price >= level2: # pris >= 300
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

elif price > level1: # pris > 100
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10


final_price = price * (100 - discount) / 100

if discount > 0:
    print("Efter rabatter blir priset....", final_price, "kr") # <-- fel concat nr med string
else:
    print("Priset blir", final_price, "kr")