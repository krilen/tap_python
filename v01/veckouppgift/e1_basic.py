"""
1 Skapa projekt och synka med GitHub

1 Skapa ett nytt Python-projekt, med ett git-repository. Skapa en fil med namnet "main.py".
När man kör filen ska programmet skriva ut följande på terminalen, fast byt ut "Ditt Namn"
mot ditt namn:
"Hello world"
"This program was made by Ditt Namn"

2 Lägg till alla ändringar till en commit.

3 Öppna inställningarna: File → Settings → Version Control → GitHub. Lägg till ditt
GitHub-konto.

4 Klicka på main-branch-ikonen. Välj alternativet "Push" och "Define remote".

5 Skapa ett repository på GitHub. Se till att det är public. Kopiera URL till repot
(webbläsarens adressfält) och skriv in i fältet "Define remote". Nu kan du synka ditt lokala
projekt med remote som är GitHub. Det gör det lätt att dela din kod mellan olika datorer.
"""


hello = "Hello world"
name = "Jack"

print(hello)
print(f"This program was made by {name}")