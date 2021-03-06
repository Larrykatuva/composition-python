# importing random
import random


# Location class
class Location:
    # Location class constructor
    def __init__(self):
        # Locations list
        locations = ["Kitchen", "Board Room", "Lounge", "Washroom", "Market", "Mall", "Library", "Lecture Hall", "Crib"]
        # Creating a location variable and assigning a random location from the locations list
        self.current_location = random.choice(locations)

    # Get current location function which returns the selected location
    def get_current_location(self):
        return self.current_location


# Suspect class
class Suspect:
    # Suspect class constructor
    def __init__(self):
        # Suspects list
        suspects = ["Miss Scarlet", "Prof Plum", "Rev Green", "Colonel Mustard", "Mrs Peacock", "Mrs White"]
        # Suspect name variable which is randomly selected from the suspects list
        self.sus_name = random.choice(suspects)
        # Location variable which is composite of class Location
        self.location = Location()

    # get current suspect function which return the selected suspect name
    def get_suspect(self):
        return self.sus_name


# Player class
class Player:
    # Player class constructor
    def __init__(self, pl_name):
        # Creating player name and assigning it to passed argument in the constructor
        self.pl_name = pl_name
        # Character variable which is composite of class Suspect
        self.character = Suspect()

    # Display function to display the results
    def display(self):
        print()
        # printing the player name
        print("Player: ", self.pl_name)
        # Printing the player character
        print("Character: ", self.character.get_suspect())
        # printing player location and weapon
        print("Location: ", self.character.location.get_current_location())


# Initializing player 1
p1 = Player("John")
# Initializing player 2
p2 = Player("Paul")

# Displaying player 1
p1.display()
# Displaying player 2
p2.display()
