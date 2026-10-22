#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: October 22 2026
# This program is a number guessing game with try catch statements

import random


def main():
    # this function is a number guessing game with try catch statements

    # Generate a random integer from 0 to 9
    random_number = random.randint(0, 9)

    # input
    integer_as_string = input("Enter a integer from 0 to 9: ")
    print("")

    # process & output
    try:
        users_guess = int(integer_as_string)
        if users_guess == random_number:
            print("You guessed the number correctly!")
        else:
            print("You entered the integer incorrectly!")
            print("The correct number was: {}.".format(random_number))
    except ValueError:
        # Fixed the misplaced parenthesis below
        print("{} is not a valid integer!".format(integer_as_string))
        print("The correct number was: {}.".format(random_number))


if __name__ == "__main__":
    main()
