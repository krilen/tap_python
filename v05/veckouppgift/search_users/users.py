"""
Söka efter användare
Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. 
Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
def autocomplete_list(input, master_list):

Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
 > AKs: * Sökniningen börjar när användaren börjar skriva i ett sökfät
        * En lista med gilltiga användare mot på vad man sökt på skall retuneras

   Krav: * Ingen skillnad mot små/stora bokstäver
         * Vid träff på en eller flera användare skall en lista med de aktuella namnen retuneras
         * Vid ingen träff skall en tom lista retuneras
         * Om input inte är en string skall None retuneras
         * Om input är tom skall None retuneras
         * Om ingen lista finns att jämnföra med skall None retuneras

   DVS None retuneras när något är fel
       En lista med många, en eller inga fulla namn retuneras i andra fall

Välj sedan ut ett AK och skriv ett testfall. (red)
Skriv sedan kod som uppfyller testfallet. (green)
Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.
"""

def autocomplete(input: str ="", master_list: list[str] =[]) -> None | list[str]:
    if not isinstance(input, str):
        return None
    
    if not input:
        return None
    
    if not master_list:
        return None

    search = input.casefold()
    usernames = [n for n in master_list if n.casefold().find(search) >= 0]
   
    return usernames



if __name__ == "__main__":
    
    print("Wrong file")