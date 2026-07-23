# Create a class called CricketPlayer.

# Requirements:

# Attributes:

# Name
# Team
# Runs
# Wickets

# Methods:

# introduce() → Print all player details.
# score_runs(runs) → Increase the player's runs.
# take_wicket() → Increase wickets by 1.

# Create two players and call all three methods.

# CricketPlayer class

# CricketPlayer class

class CricketPlayer:
    def __init__(self, name, team, runs, wickets):
        # Constructor initializes attributes
        self.name = name
        self.team = team
        self.runs = runs
        self.wickets = wickets

    def introduce(self):
        # Print all player details
        print(f"Name: {self.name}, Team: {self.team}, Runs: {self.runs}, Wickets: {self.wickets}")

    def score_runs(self, runs):
        # Increase player's runs
        self.runs += runs
        print(f"{self.name} scored {runs} runs! Total runs: {self.runs}")

    def take_wicket(self):
        # Increase wickets by 1
        self.wickets += 1
        print(f"{self.name} took a wicket! Total wickets: {self.wickets}")


# Create two players
player1 = CricketPlayer("Virat Kohli", "India", 28359, 9)
player2 = CricketPlayer("Ben Stokes", "England", 11331, 352)

# Call all three methods for each player
player1.introduce()
player1.score_runs(85)
player1.take_wicket()

print()  # Just for spacing

player2.introduce()
player2.score_runs(45)
player2.take_wicket()
