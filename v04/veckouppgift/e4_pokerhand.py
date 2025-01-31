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
    
    for suit in card_suits:
        for rank in card_ranks:
            
            card: Tuple[int, int] = suit, rank
            deck.append(card)
            
    random.shuffle(deck)
        
    return deck


# Function to check the highest "value" of your hand
def check_poker_hand(cards: list[Tuple[int, int]]) -> int:
    
    # Check to see if the cards are in sequential rank
    card_seq: bool = check_cards_seq(cards)
    
    # Check to see if the cards are of the same suit (color)
    card_same_suit: bool = check_cards_same_suit(cards)
  
    # Stright flush (same suit and sequential rank)
    if card_same_suit and card_seq:
        return 8
        
    # Stright (sequential rank)
    if card_seq:
        return 4
    
    # Flush of the same suit (color)
    if card_same_suit:
        return 5
    
    # Check to see if the cards are of the same rank (value)
    card_same_rank: str = check_cards_same_rank(cards)
    
    # Four of a kind
    if card_same_rank == "4,":
        return 7
    
    # Full house (Three of a kind and a Pair)
    elif card_same_rank == "2,3," or card_same_rank == "3,2,":
        return 6
    
    # Three of a kind
    elif card_same_rank == "3,":
        return 3
    
    # Two pair
    elif card_same_rank == "2,2,":
        return 2
    
    # Pair
    elif card_same_rank == "2,":
        return 1
    
    # Nothing, only a high card
    else:
        return 0
    

# Function to create a list of string of the cards in your hand
def pretty_hand(cards: list[Tuple[int, int]]) -> list[str]:
    hand: list[str] = []
    
    for card in cards:
        pretty_card: str = f"{card_ranks_names[card[1]]} of {card_suits_names[card[0]]}"
        hand.append(pretty_card)
        
    return hand
    

# Function to see if the rank / values of the cards in you are are sequential
def check_cards_seq(cards: list[Tuple[int, int]]) -> bool:
    ranks: list[int] = [r for _, r in cards]
    
    # Not all unique values in the list
    if len(set(ranks)) != nr_of_cards_in_hand:
        return False
    
    ranks.sort()
    
    # Compair the sorted list of cards with a range list that starts with the same value
    # as the first card in the sorted list. Equal => sequential rank (8values)
    if ranks == list(range(ranks[0], ranks[0] +nr_of_cards_in_hand)):
        return True
    
    return False


# Function to check if the cards are of the same suit (color)
def check_cards_same_suit(cards: list[Tuple[int, int]]) -> bool:
    suits: list[int] = [s for s, _ in cards]
    
    if len(set(suits)) == 1:
        return True
    
    return False


# Function to fins if cards in hand are of the same rank 8value) and how many
def check_cards_same_rank(cards: list[Tuple[int, int]]) -> str:
    ranks: list[int] = [r for _, r in cards]
    unique_ranks: list[int] = list(set(ranks))
    
    # All card values are unique => no pair, ...
    if len(unique_ranks) == nr_of_cards_in_hand:
        return "1,"
    
    pair_kind: str = ""
    
    # Loop through the unique cards and count the cards that are equal to the unique cards
    # Find cards that are of the same rank
    for unique_rank in unique_ranks:
        nr_of_same_rank: int = ranks.count(unique_rank)
        
        if nr_of_same_rank > 1:
            pair_kind += (str(nr_of_same_rank) + ",")
    
    return pair_kind


# Play one hand
def play_hand() -> Tuple[list[int], int]:
    # Create a random deck of cards
    deck_cards: list[Tuple[int, int]] = create_deck()
    
    # Get the top 5 cards for your hand
    hand_cards: list[Tuple[int, int]] = deck_cards[:nr_of_cards_in_hand]
    
    # What kind of poker hand do you have?
    poker_hand: int = check_poker_hand(hand_cards)
    
    return hand_cards, poker_hand


# Find a specific hand
def find_hand(hand_to_find: int) ->  None:
    
    # Needed since we started with 1 when showing using 'enumerate' in the menu
    hand_to_find -= 1
    
    nr_of_hands_played = 0
    
    print(f" Attempting to find: {possible_poker_hands[hand_to_find]}")
    
    while True:
        
        nr_of_hands_played += 1
        
        hand_cards, poker_hand = play_hand()
        
        if poker_hand == hand_to_find:
            break
        
        if nr_of_hands_played % nr_show_when_find == 0 or nr_of_hands_played == 1:
            print(f" {nr_of_hands_played},", end = "")

            if nr_of_hands_played % (nr_show_when_find * 10) == 0:
                print()
            
    print(f"\n\n It took {nr_of_hands_played} attempts to find the hand")
    menu_play_hand(hand_cards, poker_hand)
    
    print()
    
    
# Menu for play one hand
def menu_play_hand(hand_cards: list[Tuple[int, int]], poker_hand: int) -> None:
        
    # Make the hand of cards into strings
    hand_cards_pretty: list[str] = pretty_hand(hand_cards)
    
    # Print the card in hand
    for pretty_card in hand_cards_pretty:
        print(f"  * {pretty_card} ")
    
    # Print what kind of poker hand you have
    print(f"  > {possible_poker_hands[poker_hand]}")
    

# Menu to find a specifc hand
def menu_find_hand() -> None:
    print(" What hand do you wish to find?")

    for i, p_hand in enumerate(possible_poker_hands, start = 1):
        print(f"  {i}. {p_hand}")
        
    print("\n Press 'e' to exit this menu") 
        
    select = input("\n Select the number of the hand you wish to find >> ").casefold()
    
    if select != "e":
        try:
            find_selection: int = int(select)
            
        except ValueError:
            print("\n That was not a vaild selection!\n")
            
        else:
            if find_selection > len(possible_poker_hands) or find_selection == 0:
                print("\n That was not a vaild selection!\n")
                
            else:
                find_hand(find_selection)
            
        menu_find_hand()    
    
    
    
# Function display the main menu
def menu_print() -> None:
    
    print("\n  * Press 'p' to play a single hand.")
    print("  * Press 'f' to find how many attempts it takes")
    
    print("  * Press 'q' to quit.\n")


# Function to handle the selection of the menu
def menu_select(select: str) -> None:
    
    match select:
        
        # Play a hand
        case "p":
            hand_cards, poker_hand = play_hand()
            menu_play_hand(hand_cards, poker_hand)
            
        case "f":
            menu_find_hand()
            
        case _:
            print(" Not a valid selection!")


# Main function that controls it all
def main():
    
    print("\n ***** WELCOME TO POKER *****")
    
    while True:
    
        menu_print()
        
        select = input(" What would you like to do? >> ").casefold()
        
        if select == "q":
            break
        else:
            menu_select(select)
        
    print(" Thanks for playing")
        



if __name__ == "__main__":
    nr_of_cards_in_hand: int = 5
    card_suits: list[int] = [0, 1, 2, 3]
    card_suits_names: list[str] = ["hearts", "spade", "diamonds", "clubs"]
    card_ranks: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    card_ranks_names: list[str] = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                    "Jack", "Queen", "King", "Ace"]
    
    possible_poker_hands: list[str] = ["High card", 
                                        "Pair", 
                                        "Two pair", 
                                        "Three of a kind", 
                                        "Stright", 
                                        "Flush", 
                                        "Full house",
                                        "Four of a kind", 
                                        "Stright flush"]

    nr_show_when_find: int = 25

    # Lets run
    main()





