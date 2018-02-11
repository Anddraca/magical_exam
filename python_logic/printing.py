# will hold functions for printing the state of things based on the player's commands

# print out a welcome screen

class PrintThings:
    def printWelcome():
        for i in range(20):
            print("#", end="")
        print("\n")
        for i in range(7):
            print(" ", end="")
        print("Welcome!\n")
        for i in range(20):
            print("#", end="")
        print("\n")
