# Lab Exercise 3:Dice Simulator Using Random Module

# Dice Simulator

import random

while True:

    print("\n--- DICE SIMULATOR ---")

    input("Press Enter to Roll Dice")

    dice = random.randint(1, 6)

    print("Dice Value:", dice)

    if dice == 6:
        print("Congratulations! You got 6.")

    choice = input("Roll Again? (yes/no): ")

    if choice.lower() != "yes":
        print("Game Over!")
        break