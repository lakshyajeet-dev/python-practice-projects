# Mini Project

# Create a CricketPlayer class.

# Requirements:

# Constructor parameters:

# name
# team
# role
# runs
# wickets

# Store them using self.

# Then create three different player objects, for example:

# Jasprit Bumrah
# Virat Kohli
# Ben Stokes

# Finally, print each player's attributes using the dot operator.



# CricketPlayer class
class CricketPlayer:
    def __init__(self, name, team, role, runs, wickets):
        # Constructor initializes attributes
        self.name = name
        self.team = team
        self.role = role
        self.runs = runs
        self.wickets = wickets

# Create three player objects
player1 = CricketPlayer("Jasprit Bumrah", "India", "Bowler", 466, 506) 
player2 = CricketPlayer("Virat Kohli", "India", "Batsman", 28359, 9)
player3 = CricketPlayer("Ben Stokes", "England", "All Rounder", 11321, 352)

# Print each player's attributes using dot operator
print("Player 1:", player1.name, player1.team, player1.role, player1.runs, player1.wickets)
print("Player 2:", player2.name, player2.team, player2.role, player2.runs, player2.wickets)
print("Player 3:", player3.name, player3.team, player3.role, player3.runs, player3.wickets)
