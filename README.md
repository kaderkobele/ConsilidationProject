# Simulated War Card Game
This is a fully automated simulation of the classic card game War, played between two virtual computer players: Computer 1 and Computer 2. Built with Python, it showcases fundamental programming concepts like functions, loops, conditionals, and file I/O.
##  How the Simulation Works
- A standard 52-card deck is shuffled and split evenly.
- Each round, both computers automatically play their top card.
- The computer with the higher card value wins the round and takes both cards.
- If the cards tie in value, both are discarded.
- The first computer to win 10 rounds wins the game.
## Stats Tracking
- After each simulation, the winner's name is logged to a file called `stats.txt`.
- Stats persist between runs and can be viewed any time after a game.
## Features
- Fully autonomous you just sit back and observe the simulation.
- Win tracking saved between sessions using file storage.
- Game logic implemented using basic Python structures.
- Clean command-line interface with options after each match.