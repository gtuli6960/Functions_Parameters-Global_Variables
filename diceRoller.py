# Dice roll program.

# Import external libraries.
import random,time

# Define a list containing the dice faces.
faces = ["- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n","- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n","- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n","- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n","- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n","- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"]

# Roll the dice.
def roll():
    print("rolling.....")
    number = random.randint(0,5)
    return number

# Output (show) the dice.
def show_dice(number):
    print(faces[number])

# A variable to hold the previous roll.
previous = -1

# While loop to detect if the previous roll was a 6.
while previous != 5:
    number = roll()
    previous = number
    time.sleep(0.1)
    show_dice(number)

# Win script.
print("You rolled a six.  Well done.")


# Changed the top comment to relate to the program.
# Fixed the import errors.
# Adjusted the functions to work correctly with each other.
# Added functionality so when a six is rolled the user wins.
# Made the whole program more efficient by using a list to contain the dice faces, and a single line of code to deal with the generated number and output the dice face.
