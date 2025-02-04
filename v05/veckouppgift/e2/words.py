"""
2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. 
Ett ord är en serie tecken som separeras av mellanslag. 
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
 > * User story: "som en användare när jag skriver in min mening så vill jag veta hur många ord det är"
   * Tasks:
      - T1: När något skrivs in skall antal ord räknas
   * Task: När något skrivs in skall antal ord räknas
      - AK1: Användaren skall få i realtid tillbaka hur många ord det är utan att trycka på enter
      - AK2: Antal ord som finns i mening skall retuneras
   * AK2 och AK3
      - Säkerställ att input är en "string" annars görs inget
      - Retunerar antal ord (skiljetecken mellanrum) som finns i input
      - annars skall None retuneras
   * Krav
      - Om input inte är en "string" skall None retuneras
      - Om input är tom skall None retuneras
      - Antal ord i input skall retuneras
      - annars None


2b Skriv testfall som testar alla AK.

2c Implementera funktionen, så att alla testfall blir gröna.


"""

def count_words(sentence: str = "") -> int | None:

    if not isinstance(sentence, str):
        return None

    if not sentence:
        return None
    
    count_words = sentence.split()
    
    if len(count_words) > 0:
        return len(count_words)
    
    return None
