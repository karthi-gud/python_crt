##Design a backend system to manage multiplayer game tournaments. Pla play matches, and earn points. The system should rank them, handle and simulate knockout rounds.
#Features:
#layer registration with unique usernames.
#Match results entry and automatic point updates.
#Leaderboard sorted by score.
#Simulate knockout using recursion.
#Export match history.
#Tech Stack:
#- -
#Core Python (Lists, Dictionaries, Tuples)
#OOP (Player, Match, Tournament classes)
#Recursion (Knockout simulation)
#Sorting Algorithms (Leaderboard)
#File Handling (History logs)
#Optional: pandas for final score export



import random

players = {}
matches = []
n = int(input("Enter number of players: "))
for _ in range(n):
    name = input("Enter player name: ")
    players[name] = 0
m = int(input("Enter number of matches: "))
for _ in range(m):
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")
    winner = input("Winner: ")
    players[winner] += 3
    matches.append(f"{p1} vs {p2} → Winner: {winner}")
print("\nLeaderboard:")
sorted_players = sorted(players.items(), key=lambda x: (-x[1], x[0]))
for name, points in sorted_players:
    print(f"{name}: {points} points")
def knockout(player_list):
    if len(player_list) == 1:
        print("\nWinner of Knockout:", player_list[0])
        return
    next_round = []
    print("\nKnockout Round:")
    for i in range(0, len(player_list), 2):
        if i + 1 < len(player_list):
            winner = random.choice([player_list[i], player_list[i+1]])
            print(f"{player_list[i]} vs {player_list[i+1]} → Winner: {winner}")
            next_round.append(winner)
        else:
            print(f"{player_list[i]} gets a bye")
            next_round.append(player_list[i])
    knockout(next_round)
knockout(list(players.keys()))
with open("match_history.txt", "w") as f:
    for match in matches:
        f.write(match + "\n")
print("\nMatch history saved to match_history.txt")  