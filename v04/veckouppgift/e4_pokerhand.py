"""
Pokerhand
När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. 
Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. 
Exempel på körning:
poker_hand(cards) -> "Du fick ett par med valören: 5"

1. Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör.
Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
Exempel på ett kort: 
["hjärter", 12]

> Valde att istället skapa en hel korthög med alla färger och värden och sedan blanda dem.
  Detta för att säkerställa att de inte finns två kort av samma färg och värde.  

2. Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

> Gick of topic här slutförde uppgiften på mitt egna sätt

3. Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda 
på om man har ett par, dvs det finns två kort med samma valör.

Fortsätt att lägga till fler kontroller till funktionen.
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
pretty_print_card(["hjärter", 5]) → "hjärter fem"

Lista med pokerhänder:
 * Ett par (två lika kort)
 * Två par
 * Tretal (tre lika)
 * Straight (5 kort i följd, t.ex. 7-8-9-10-11)
 * Flush / färg (alla kort har samma färg)
 * Hus (par och tretal med olika valörer)
 * Fyrtal
 * Straight flush (5 kort i följd, med samma färg)
 * Femtal <-- Detta finns inte om man inte använder vilda kort

"""
from typing import Tuple
import random


# Function that creates a random deck of cards
def create_deck() -> list[Tuple[int, int]]:
    deck: list[Tuple[int, int]] = []
    
    for color in card_colors:
        for value in card_values:
            
            card: Tuple[int, int] = color, value
            deck.append( card )
            
    random.shuffle(deck)
        
    return deck
    

# Function to check the highest "value" of your hand
def check_poker_hand(cards: list[Tuple[int, int]]) -> int:
    
    # Check to see it the cards are in sequential rank
    card_seq: bool = check_cards_seq(cards)
  
    # Stright flush (same color and sequential rank)
    if cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0] and card_seq:
        return 8
        
    # Stright (sequential rank)
    if card_seq:
        return 4
    
    # Flush (same color)
    if cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0]:
        return 5
    
    # Check to see if the cards are of the same values
    card_same_value: str = check_cards_same_value(cards)
    
    # Four of a kind
    if card_same_value == "4,":
        return 7
    
    # Full house (Three of a kind and a Pair)
    elif card_same_value == "2,3," or card_same_value == "3,2,":
        return 6
    
    # Three of a kind
    elif card_same_value == "3,":
        return 3
    
    # Two pair
    elif card_same_value == "2,2,":
        return 2
    
    # Pair
    elif card_same_value == "2,":
        return 1
    
    # Nothing, only a high card
    else:
        return 0
    

# Function to create a list of string of the cards in your hand
def pretty_hand(cards: list[Tuple[int, int]]) -> list[str]:
    hand: list[str] = []
    
    for card in cards:
        pretty_card: str = f"{card_values_names[card[1]]} of {card_colors_names[card[0]]}"
        hand.append(pretty_card)
        
    return hand
    

# Function to see if the rank / values of the cards in you are are sequential
def check_cards_seq(cards: list[Tuple[int, int]]) -> bool:
    values: list[int] = [v for _, v in cards ]
    
    # Not all unique values in the list
    if len(set(values)) != 5:
        return False
    
    values.sort()
    
    # Compair the sorted list of cards with a range list that starts with the same value
    # as the first card in the sorted list. Equal => sequential rank (8values)
    if values == list(range(values[0], values[0]+5)):
        return True
    
    return False


def check_cards_same_value(cards: list[Tuple[int, int]]) -> str:
    values: list[int] = [v for _, v in cards ]
    unique_values: list[int] = list(set(values))
    
    # All card values are unique => no pair, ...
    if len(unique_values) == 5:
        return "1,"
    
    pair_kind: str = ""
    
    # Loop through the unique cards and count the cards that are equal to the unique cards
    for unique_value in unique_values:
        nr_of_same_value: int = values.count(unique_value)
        
        if nr_of_same_value > 1:
            pair_kind += (str(nr_of_same_value) + ",")
    
    return pair_kind



# Main function that controls it allk
def main():
    # Create a random deck of cards
    deck_cards: list[Tuple[int, int]] = create_deck()

    hand_cards: list[Tuple[int, int]] = deck_cards[:5]
    
    poker_hand: int = check_poker_hand(hand_cards)
    hand_cards_pretty: list[str] = pretty_hand(hand_cards)
    
    # Print the card in hand
    for pretty_card in hand_cards_pretty:
        print(f" * {pretty_card} ")
    
    # Print what kind of poker hand you have
    print(f" >>> {possible_poker_hands[poker_hand]}")


if __name__ == "__main__":
    card_colors: list[int] = [0, 1, 2, 3]
    card_colors_names: list[str] = ["hearts", "spade", "diamonds", "clubs"]
    card_values: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    card_values_names: list[str] = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                    "Knight", "Queen", "King", "Ace"]
    
    possible_poker_hands: list[str] = ["High card", 
                                        "Pair", 
                                        "Two pair", 
                                        "Three of a kind", 
                                        "Stright", 
                                        "Flush", 
                                        "Full house", 
                                        "Four of a kind", 
                                        "Stright flush"]

    # Lets run
    main()





