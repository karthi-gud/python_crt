#write a python program to read a year as input from thr year and check wether it is a leap year or not 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

Design a backend system to manage multiplayer game tournaments. Pla play matches, and earn points. The system should rank them, handle and simulate knockout rounds.
Features:
Player registration with unique usernames.
Match results entry and automatic point updates.
Leaderboard sorted by score.
Simulate knockout using recursion.
Export match history.
Tech Stack:
- -
Core Python (Lists, Dictionaries, Tuples)
OOP (Player, Match, Tournament classes)
Recursion (Knockout simulation)
Sorting Algorithms (Leaderboard)
File Handling (History logs)
Optional: pandas for final score export