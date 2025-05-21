# Import random so that it can be used in the function
import random
import sys
import os

# Create a tuple with all of the card suits
card_suits = ('Spades', 'Clubs', 'Diamonds', 'Heart')
# Create a tuple with all of the card types
card_types = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen','King', 'Ace')
# create a deck of cards

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

while True:
    # Reset deck and hands every game
    deck = []
    for suit in card_suits:
        for card in card_types:
            deck.append((card, suit))
    random.shuffle(deck)
    Player_1hand = deck[:26]
    Player_2hand = deck[26:]
    playerOneScore = 0
    playerTwoScore = 0
    rounds = 1


    def compare_cards(val1, val2):
        # Compares the card's values
        if val1 > val2:
            return 1
        elif val2 > val1:
            return 2
        else:
            return 0
        #   TEST CASES FOR COMPARE CARDS
        # print(compare_cards(10, 5))    # Expected: 1 (Player 1 wins)
        # print(compare_cards(4, 11))    # Expected: 2 (Player 2 wins)
        # print(compare_cards(7, 7))     # Expected: 0 (Tie)
        # print(compare_cards(14, 13))   # Expected: 1 (Ace > King)
        # print(compare_cards(2, 2))     # Expected: 0 (tie)

    
    def update_stats(winner):
        # Updates the stats of the stats.txt file
        stats = {"Player 1": 0, "Player 2": 0}
        if os.path.exists("stats.txt"):
            with open("stats.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    name, count = line.strip().split(":")
                    stats[name] = int(count)

        stats[winner] += 1
        with open("stats.txt", "w") as f:
            for key in stats:
                f.write(f"{key}:{stats[key]}\n")

    def read_stats():
    # Prints the user's stats
        print("\n📊 Game Statistics:")
        try:
            if not os.path.exists("stats.txt"):
                print("No stats recorded yet.")
                return
            with open("stats.txt", "r") as f:
                for line in f:
                    name, count = line.strip().split(":")
                    print(f"{name} Wins: {count}")
        except Exception as e:
            print(f"⚠️ Error reading stats: {e}")



    print("""
    ====================================
    🤖 Simulated War Card Game 🤖
    ====================================

    Welcome! This program simulates a game of War between two computer players:
    🖥️ Computer 1 vs. 🖥️ Computer 2

    🔁 How it works:
    - Each computer is dealt half of a shuffled 52-card deck (26 cards).
    - In each round, both computers automatically play their top card.
    - The computer with the higher card value wins the round and collects both cards.
    - If there is a tie, both cards are discarded.

    🏁 Game Objective:
    - The first computer to win 10 rounds wins the simulated game.

    📊 After the game ends, you'll have the option to:
    1. Run another simulation
    2. View win statistics
    3. Exit the program

    Press ENTER to begin the simulation...
    """)
    input()

    while len(Player_1hand) != 0 and len(Player_2hand) != 0:
        print(f"\nRound {rounds}")
        card1 = Player_1hand.pop(0)
        card2 = Player_2hand.pop(0)
        print(f"Player 1 plays {card1}")
        print(f"Player 2 plays {card2}")
        
        val1 = card_values[card1[0]]
        val2 = card_values[card2[0]]
        if(compare_cards(val1, val2)) == 1:
            print("Player 1 wins the round!")
            playerOneScore += 1
            random.shuffle(Player_1hand)
            Player_1hand.extend([card1, card2])
        elif(compare_cards(val1, val2)) == 2:
            print("Player 2 wins the round!")
            playerTwoScore += 1
            random.shuffle(Player_2hand)
            Player_2hand.extend([card1, card2])
        else:
            print("It's a tie! Cards are discarded.")


        rounds += 1

        if playerOneScore == 10:
            print("\n🎉 Player 1 wins the game!")
            update_stats("Player 1")
            
            print("\nWhat would you like to do next?")
            print("1. Play again")
            print("2. View game stats")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                break
            if choice == "2":
                read_stats()
                sys.exit()
            if choice == "3":
                print("Thanks for playing!")
                sys.exit()
            if choice != "1" or choice != "2" or choice != "3":
                print("Invalid choice. Exiting.")
                sys.exit()
        if playerTwoScore == 10:
            print("\n🎉 Player 2 wins the game!")
            update_stats("Player 2")
            
            print("\nWhat would you like to do next?")
            print("1. Play again")
            print("2. View game stats")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                break
            if choice == "2":
                read_stats()
                sys.exit()
            if choice == "3":
                print("Thanks for playing!")
                sys.exit()
            if choice != "1" or choice != "2" or choice != "3":
                print("Invalid choice. Exiting.")
                sys.exit()