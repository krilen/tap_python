"""
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
 * sätta in pengar (deposit)
 * ta up pengar (withdraw)
 * returnera nuvarande saldo (balance)
 * räkna ut ränta (apply_interest, lägger till räntan till kontot)
 * tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.

User stories
 * "som kund vill jag kunna hantera mina pengar så att jag kan göra olika saker med dem"
 * "som kund vill jag kunna sätta in så att jag kan spara pengar på mitt konto"
 * "som kund vill jag ta ut pengar från mitt konto så att jag kan använda dem"
 * "som kund vill jag se balansen på mitt konto så att jag ser hur mycket pengar jag har"
 * "som kund vill jag få ränta på mitt konto så att det är lönsamt att spara pengar
 * "som kund vill jag kontrollera täckning så att jag kan se om jag kan betala faktura med mina pengar"
 * "som kund vill jag se hur olika räntor påverkar mitt konto så det är möjligt se hur det kan gå för mina pengar"
 
Extra 
 * "som kund vill jag kunna välja ur en meny så att det det blir enklare att göra olika saker"
 * "som kund vill jag kunna ha olika konto så att jag kan plasera pengarna på olika ställen"




US: "som kund vill jag kunna hantera mina pengar så att jag kan göra olika saker med dem"
Acceptanskriterier
 * "Minst ett konto behöver finnas för att kunna använda applikationen"
 * "Man skall bara kunna se sina egna konton inte andras"
 * "Om inga konton finns skall det inte vara möjligt att använda applikationen"

Övriga krav
 * "Om inget konto finns skall 'None' retuneras och man skall inte kunna göra något"
 * "Vid laddning av ens konto skall det placeras i en lista för att säkerställa framtida konton"
 * "Varje konto skall ha ett namn, aktuell saldo och räntesats
 



"""



from account import *
from client import *
from menu import *



def main():
    client = Client()
    
    
    print(" ***** Welcome to simple ATM *****")

    """
    while True:
        
        select: str = input("\n Choose what you want to do >> ")
        
        
        
        if select == "q":
            break
        

    print("\n Thank you for using simple ATM\n")
    """
    
  
    client_account = client.get_client_account("jack")
    
    if isinstance(client_account, list):
        pass
    
    print(type(client_account))

    client_account = client.get_client_account("mike")
    
    print(client_account)
    
    del(client)

if __name__ == "__main__":
    main()